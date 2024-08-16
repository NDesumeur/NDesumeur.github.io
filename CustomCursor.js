

document.addEventListener('DOMContentLoaded', function () {
    var customCursor = document.createElement('div');
    customCursor.classList.add('custom-cursor');
    document.body.appendChild(customCursor);

    var trail = document.createElement('div');
    trail.classList.add('trail');
    document.body.appendChild(trail);

    document.addEventListener('mousemove', function (e) {
        customCursor.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
        trail.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;

        trail.style.width = '30px';
        trail.style.height = '30px';

        clearTimeout(trail.timeout);
        trail.timeout = setTimeout(function () {
            trail.style.width = '20px';
            trail.style.height = '20px';
        }, 100);
    });
});
