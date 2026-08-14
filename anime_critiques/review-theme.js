document.addEventListener('DOMContentLoaded', function () {
    function getCurrentHost() {
        return window.location && window.location.hostname ? window.location.hostname : '';
    }

    function isExternalLink(anchor) {
        if (!anchor || !anchor.href) {
            return false;
        }

        try {
            var url = new URL(anchor.href, window.location.href);
            return url.protocol === 'http:' || url.protocol === 'https:' ? url.hostname !== getCurrentHost() : false;
        } catch (error) {
            return false;
        }
    }

    function openExternalLinksInNewTab() {
        var anchors = document.querySelectorAll('a[href]');

        anchors.forEach(function (anchor) {
            if (isExternalLink(anchor)) {
                anchor.setAttribute('target', '_blank');
                anchor.setAttribute('rel', 'noopener noreferrer');
            }
        });
    }

    openExternalLinksInNewTab();

    var ratingElement = document.querySelector('.rating');

    if (!ratingElement) {
        return;
    }

    var rating = parseFloat(String(ratingElement.textContent || '').replace(',', '.'));

    if (Number.isNaN(rating)) {
        return;
    }

    var accent = '#f5a524';
    var accentSoft = 'rgba(245, 165, 36, 0.14)';
    var accentShadow = 'rgba(245, 165, 36, 0.24)';
    var ratingText = '#111111';

    function hexToRgb(hex) {
        var normalized = hex.replace('#', '');
        return {
            red: parseInt(normalized.slice(0, 2), 16),
            green: parseInt(normalized.slice(2, 4), 16),
            blue: parseInt(normalized.slice(4, 6), 16)
        };
    }

    function getContrastTextColor(hex) {
        var rgb = hexToRgb(hex);
        var luminance = (0.2126 * rgb.red + 0.7152 * rgb.green + 0.0722 * rgb.blue) / 255;
        return luminance >= 0.58 ? '#111111' : '#ffffff';
    }
    function hslToHex(hue, saturation, lightness) {
        var s = saturation / 100;
        var l = lightness / 100;
        var chroma = (1 - Math.abs(2 * l - 1)) * s;
        var segment = hue / 60;
        var intermediate = chroma * (1 - Math.abs(segment % 2 - 1));
        var red = 0;
        var green = 0;
        var blue = 0;

        if (segment >= 0 && segment < 1) {
            red = chroma;
            green = intermediate;
        } else if (segment < 2) {
            red = intermediate;
            green = chroma;
        } else if (segment < 3) {
            green = chroma;
            blue = intermediate;
        } else if (segment < 4) {
            green = intermediate;
            blue = chroma;
        } else if (segment < 5) {
            red = intermediate;
            blue = chroma;
        } else {
            red = chroma;
            blue = intermediate;
        }

        var match = l - chroma / 2;
        var toHex = function (value) {
            return Math.round((value + match) * 255).toString(16).padStart(2, '0');
        };

        return '#' + toHex(red) + toHex(green) + toHex(blue);
    }

    if (rating < 1) {
        accent = '#7f1d1d';
        accentSoft = 'rgba(127, 29, 29, 0.18)';
        accentShadow = 'rgba(127, 29, 29, 0.30)';
    } else {
        var hue;

        if (rating < 4) {
            hue = (rating - 1) * 6;
        } else if (rating < 6) {
            hue = 18 + (rating - 4) * 9;
        } else if (rating < 8) {
            hue = 36 + (rating - 6) * 12;
        } else {
            hue = 60 + (rating - 8) * 30;
        }

        hue = Math.max(0, Math.min(120, Math.round(hue)));
        accent = hslToHex(hue, 78, rating >= 8 ? 48 : 50);
        accentSoft = 'hsla(' + hue + ', 78%, 50%, 0.16)';
        accentShadow = 'hsla(' + hue + ', 78%, 50%, 0.28)';
    }

    ratingText = getContrastTextColor(accent);

    var synopsisTitles = document.querySelectorAll('.review-box .title');
    synopsisTitles.forEach(function (titleElement) {
        if (titleElement.textContent.trim().toLowerCase() === 'synopsis') {
            var reviewParagraph = titleElement.previousElementSibling;
            if (reviewParagraph && reviewParagraph.tagName === 'P' && reviewParagraph.className !== 'title') {
                reviewParagraph.remove();
            }
        }
    });

    document.body.style.setProperty('--accent', accent);
    document.body.style.setProperty('--accent-soft', accentSoft);
    document.body.style.setProperty('--accent-shadow', accentShadow);
    document.body.style.setProperty('--rating-text', ratingText);
});