
# Default fonts in Operating Systems

# References 

[FontsAreana Original Source](https://fontsarena.com/blog/operating-systems-default-sans-serif-fonts/)


---
# Operating systems default sans-serif fonts 

No doubt that you’ve probably seen a css font-family declaration that
didn’t include a specific webfont, but just the `sans-serif` fallback,
or values like `-apple-system`, `system-ui`, and `BlinkMacSystemFont`.

All of those values will return the operating system’s default
sans-serif font, with some differences:

-   `-apple-system` works only for newer MacOS versions (El Capitan and
    newer) and iOS
-   `BlinkMacSystemFont` works only for older Mac OS versions (Yosemite
    and older)
-   `system-ui` works for all operating systems, but there’s one notable
    exception: it doesn’t work in the Firefox browser. Firefox doesn’t
    support this value, so your text will be displayed in the default
    fallback which is a serif font
-   `sans-serif` will work in all browsers and operating systems, but
    should be only used as fallback, because in some cases operating
    systems have quirks like different sans font set for web than in its
    interface

Whether you use a custom font or not, the recommended complete css
font-family declaration is:

`font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu, "Helvetica Neue", Oxygen, Cantarell, sans-serif;`

You can safely omit Oxygen and Cantarell since they are targeted to
certain Linux versions only. `Roboto, Ubuntu, sans-serif` will be ok for
Linux distros.

Default sans-serif font in MacOS {.section-title}
--------------------------------

MacOS (El Capitan and newer)

San Francisco

MacOS (Yosemite)

Helvetica Neue

MacOS (older versions)

Lucida Grande

Please note that — although for interface San Francisco is the default
sans-serif font — for web `-apple-system` will need to be used, as the
`sans-serif` fallback will display Helvetica instead of San Francisco.
(this is one of the quirks I mentioned earlier)

Default sans-serif font in Windows {.section-title}
----------------------------------

The difference between Microsoft Sans Serif and MS Sans Serif is that MS
Sans Serif was a bitmap/raster font available in 8, 10, 12, 14, 18, and
24 sizes and Microsoft Sans Serif is a TrueType scalable font.

MS Sans Serif was based on Helvetica and in all versions up to Windows
3.1 it was called Helv.

Windows (Vista and newer, including Windows 10)

Segoe UI

Windows (XP)

Tahoma

Windows (2000)

Microsoft Sans Serif

Windows (95, NT, Millennium)

MS Sans Serif

Windows (older versions including Windows 3)

Helv

Default sans-serif font in Linux {.section-title}
--------------------------------

Many Linux users re-configure defaults to other fonts like [Inter
UI](https://fontsarena.com/inter-ui-by-rasmus-andersson/) or others. So
it’s almost impossible to accurately mention defaults, except for the
Ubuntu distro which has its own font as default. Red Hat also has
commissioned its own fonts, Red Hat Display and Red Hat Text.

Ubuntu

Ubuntu

Red Hat

[Red
Hat](https://fontsarena.com/red-hat-display-and-text-by-jeremy-mickel/)

Other distros (Arch Linux, Debian, Fedora etc.)

It varies, can be DejaVu Sans, Noto Sans, Liberation Sans etc.

Default sans-serif font in iOS and iPadOS {.section-title}
-----------------------------------------

iOS (9 and newer)and iPadOS

San Francisco

iOS (8 and older)

Helvetica/Helvetica Neue

Default sans-serif font in watchOS {.section-title}
----------------------------------

watchOS

San Francisco Compact

Default sans-serif font in Android {.section-title}
----------------------------------

Android (4.0+)

Roboto

Android (older versions)

Droid Sans


