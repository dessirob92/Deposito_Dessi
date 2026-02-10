// --- 1. INIZIALIZZAZIONE GSAP E PLUGINS ---
gsap.registerPlugin(ScrollTrigger);

// --- 2. LOGICA DEL CURSORE CUSTOM ---
const cursor = document.querySelector('.custom-cursor');

document.addEventListener('mousemove', (e) => {
    // Muoviamo il cursore con un leggero ritardo per un effetto fluido
    gsap.to(cursor, {
        x: e.clientX,
        y: e.clientY,
        duration: 0.1,
        ease: "power2.out"
    });
});

// Effetto interattivo sui link e bottoni
const links = document.querySelectorAll('a, button');
links.forEach(link => {
    link.addEventListener('mouseenter', () => {
        gsap.to(cursor, {
            scale: 4,
            backgroundColor: "rgba(212, 175, 55, 0.1)", // Electric Gold semi-trasparente
            border: "1px solid #d4af37",
            duration: 0.3
        });
    });
    
    link.addEventListener('mouseleave', () => {
        gsap.to(cursor, {
            scale: 1,
            backgroundColor: "#d4af37",
            border: "none",
            duration: 0.3
        });
    });
});

// --- 3. ANIMAZIONE HERO SECTION (ENTRATA) ---
const tlHero = gsap.timeline();

tlHero.from(".logo", {
    y: -50,
    opacity: 0,
    duration: 1.2,
    ease: "expo.out"
})
.from(".glitch-text", {
    y: 100,
    opacity: 0,
    duration: 1.5,
    ease: "power4.out"
}, "-=0.8")
.from(".subtitle", {
    opacity: 0,
    duration: 1,
}, "-=1")
.from(".canvas-container", {
    scale: 0.8,
    opacity: 0,
    duration: 2,
    ease: "expo.out"
}, "-=1.5");

// --- 4. SCROLL ANIMATIONS (EFFETTO RIVELAZIONE) ---
// Animazione per le sezioni che appaiono allo scroll
gsap.utils.toArray('.split-section').forEach(section => {
    gsap.from(section.querySelectorAll('.text-block > *'), {
        scrollTrigger: {
            trigger: section,
            start: "top 80%", // Parte quando la sezione è all'80% del viewport
            toggleActions: "play none none reverse"
        },
        y: 50,
        opacity: 0,
        duration: 1,
        stagger: 0.2, // Fa apparire gli elementi uno dopo l'altro
        ease: "power3.out"
    });

    gsap.from(section.querySelector('.parallax-img'), {
        scrollTrigger: {
            trigger: section,
            start: "top bottom",
            end: "bottom top",
            scrub: true // L'animazione segue il movimento dello scroll
        },
        y: -100,
        scale: 1.1,
        ease: "none"
    });
});

// --- 5. LOGICA "WATCH DISCOVERY" (SMONTAGGIO VIRTUALE) ---
// Immaginiamo che scrollando la sezione engineering, l'orologio si apra
gsap.to(".canvas-container", {
    scrollTrigger: {
        trigger: "#engineering",
        start: "top bottom",
        end: "bottom top",
        scrub: 1
    },
    x: "-25%", // Sposta l'orologio a sinistra per lasciare spazio al testo
    rotation: 45,
    filter: "brightness(1.5) drop-shadow(0 0 20px #d4af37)"
});

console.log("AETERNA Engine: Active. Status: Elite.");



// Animazione speciale per l'apparizione della sezione contatti
        gsap.from("#concierge .glass", {
            scrollTrigger: {
                trigger: "#concierge",
                start: "top 80%",
            },
            y: 60,
            opacity: 0,
            duration: 1.5,
            ease: "power4.out"
        });

        // Aggiorna il cursore per gli elementi del form
        document.querySelectorAll('.contact-input').forEach(el => {
            el.addEventListener('mouseenter', () => gsap.to(cursor, { scale: 2.5, backgroundColor: "rgba(212,175,55,0.05)", border: "1px solid #d4af37" }));
            el.addEventListener('mouseleave', () => gsap.to(cursor, { scale: 1, backgroundColor: "#d4af37", border: "none" }));
        });