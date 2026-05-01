# README banners & badge references

Deze folder verzamelt de dynamische image-URLs en badge-formaten die in de bovenliggende `README.md` gebruikt worden. Door ze hier te documenteren blijft de README compact en kunnen we kleuren of varianten centraal aanpassen.

Alle banners worden on-demand gerenderd door [kyechan99/capsule-render](https://github.com/kyechan99/capsule-render). Alle statische badges komen van [shields.io](https://shields.io).

## Header banner (boven in README)

```
https://capsule-render.vercel.app/api?type=waving&color=0:0a7ea4,50:0b1f2a,100:6264a7&height=220&section=header&text=XML%2FXSD%20Contract%20Hub&fontSize=52&fontAlignY=38&fontColor=ffffff&desc=Source%20of%20Truth%20%E2%80%A2%20Integration%20Project%20Groep%201&descAlignY=62&descSize=18&animation=fadeIn
```

Belangrijke parameters:

| Param        | Effect                                                  |
|--------------|---------------------------------------------------------|
| `type`       | `waving`, `rect`, `slice`, `cylinder`, `soft`, `egg`    |
| `color`      | Single hex of gradient (`0:AAA,50:BBB,100:CCC`)         |
| `height`     | Hoogte in pixels                                        |
| `text`       | URL-encoded titel                                       |
| `desc`       | URL-encoded ondertitel                                  |
| `animation`  | `fadeIn`, `twinkling`, `blinking`, `scaleIn`            |

## Section divider (tussen developer- en maintainersectie)

```
https://capsule-render.vercel.app/api?type=rect&color=0:0a7ea4,100:6264a7&height=4&section=header
```

## Footer banner

```
https://capsule-render.vercel.app/api?type=waving&color=0:6264a7,50:0b1f2a,100:0a7ea4&height=120&section=footer
```

## Badge palet

De badges in de README delen één donkere `labelColor` (`0b1f2a`) zodat alles als één samenhangende set aanvoelt.

| Type           | Stijl              | Voorbeeld                                                                          |
|----------------|--------------------|------------------------------------------------------------------------------------|
| Hero / kernrol | `for-the-badge`    | `Contract-v2.4-0a7ea4?style=for-the-badge&logo=files&logoColor=white&labelColor=0b1f2a` |
| Status         | `flat-square`      | `Build-passing-2f855a?style=flat-square&logo=githubactions&logoColor=white&labelColor=0b1f2a` |
| Legende-kleur  | `flat-square` (leeg) | `-%20-10b981?style=flat-square` (groen vlakje voor de mermaid-legende)             |

## Editing rules

- Houd `labelColor=0b1f2a` consistent over alle badges.
- Gebruik **groen** (`2f855a`) voor "actief / passing", **oranje** (`f59e0b`) voor "let op / bijgewerkt", **rood** (`c53030`) voor "enforcement / governance".
- Nieuwe banners → URL hier documenteren zodat het team ze kan hergebruiken.
