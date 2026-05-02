// gen-badges — generates flat SVG status badges for the XML/XSD Contract Hub.
//
// Usage:
//
//	go run main.go                    # writes to ../badges/
//	go run main.go path/to/output/    # writes to a custom directory
//
// Each badge follows the shields.io flat style:
//
//	[ team label ][ status value ]
//
// with the project dark-blue (#0b1f2a) on the left and a status colour on the right.
package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
	"text/template"
)

// badge holds the data for one SVG badge.
type badge struct {
	Label      string
	Value      string
	Color      string
	LabelWidth int
	ValueWidth int
}

func (b badge) Total() int  { return b.LabelWidth + b.ValueWidth }
func (b badge) LabelCX() int { return b.LabelWidth / 2 }
func (b badge) ValueCX() int { return b.LabelWidth + b.ValueWidth/2 }

const svgTpl = `<svg xmlns="http://www.w3.org/2000/svg" width="{{.Total}}" height="20" role="img" aria-label="{{.Label}}: {{.Value}}">
  <title>{{.Label}}: {{.Value}}</title>
  <clipPath id="r"><rect width="{{.Total}}" height="20" rx="3" fill="#fff"/></clipPath>
  <g clip-path="url(#r)">
    <rect width="{{.LabelWidth}}" height="20" fill="#0b1f2a"/>
    <rect x="{{.LabelWidth}}" width="{{.ValueWidth}}" height="20" fill="{{.Color}}"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
    <text x="{{.LabelCX}}" y="14.5">{{.Label}}</text>
    <text x="{{.ValueCX}}" y="14.5">{{.Value}}</text>
  </g>
</svg>
`

// charWidth returns an approximate pixel width for a single character at
// font-size 11 in Verdana, used to size badge label/value sections.
func charWidth(c rune) int {
	switch {
	case c == 'i' || c == 'l' || c == '1' || c == '.' || c == ':' || c == '|':
		return 5
	case c == 'm' || c == 'w' || c == 'M' || c == 'W':
		return 9
	case c >= 'A' && c <= 'Z':
		return 8
	default:
		return 7
	}
}

// sectionWidth calculates the pixel width for a label/value string including
// 5 px padding on each side.
func sectionWidth(s string) int {
	w := 10 // 5 left + 5 right padding
	for _, c := range s {
		w += charWidth(c)
	}
	return w
}

// colors
const (
	colorConform  = "#2f855a"
	colorKritiek  = "#c53030"
	colorAlert    = "#b45309"
	colorExcept   = "#2f855a"
)

var teamBadges = []struct {
	name   string
	status string
	color  string
}{
	{"kassa", "CONFORM", colorConform},
	{"crm", "KRITIEK", colorKritiek},
	{"frontend", "KRITIEK", colorKritiek},
	{"planning", "CONFORM", colorConform},
	{"facturatie", "KRITIEK", colorKritiek},
	{"monitoring", "ALERT", colorAlert},
	{"mailing", "CONFORM", colorConform},
	{"identity-service", "CONFORM", colorExcept},
	{"heartbeat", "KRITIEK", colorKritiek},
}

func main() {
	outDir := filepath.Join("..", "badges")
	if len(os.Args) > 1 {
		outDir = os.Args[1]
	}

	if err := os.MkdirAll(outDir, 0o755); err != nil {
		fmt.Fprintf(os.Stderr, "error: mkdir %s: %v\n", outDir, err)
		os.Exit(1)
	}

	tmpl := template.Must(template.New("badge").Parse(svgTpl))

	for _, t := range teamBadges {
		b := badge{
			Label:      t.name,
			Value:      t.status,
			Color:      t.color,
			LabelWidth: sectionWidth(t.name),
			ValueWidth: sectionWidth(t.status),
		}
		fname := filepath.Join(outDir, t.name+"-"+strings.ToLower(t.status)+".svg")
		f, err := os.Create(fname)
		if err != nil {
			fmt.Fprintf(os.Stderr, "error: create %s: %v\n", fname, err)
			continue
		}
		err = tmpl.Execute(f, b)
		f.Close()
		if err != nil {
			fmt.Fprintf(os.Stderr, "error: render %s: %v\n", fname, err)
			continue
		}
		fmt.Printf("  wrote %s  (%dpx)\n", fname, b.Total())
	}
}
