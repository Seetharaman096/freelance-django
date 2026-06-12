// ── MOBILE HAMBURGER MENU ──
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('open');
  hamburger.classList.toggle('active');
});

// Close menu when a nav link is clicked
document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    hamburger.classList.remove('active');
  });
});


// ── HAMBURGER ANIMATION ──
const style = document.createElement('style');
style.textContent = `
  .hamburger.active span:nth-child(1) {
    transform: rotate(45deg) translate(5px, 6px);
  }
  .hamburger.active span:nth-child(2) {
    opacity: 0;
  }
  .hamburger.active span:nth-child(3) {
    transform: rotate(-45deg) translate(5px, -6px);
  }
`;
document.head.appendChild(style);


// ── SMOOTH SCROLL ──
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});


// ── SCROLL ANIMATION ──
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.05, rootMargin: '0px 0px -40px 0px' });

window.addEventListener('load', () => {
  document.querySelectorAll('.card, .service-item, .skill-card, .fact-card, .info-item').forEach(el => {
    el.classList.add('fade-in');
    observer.observe(el);
  });
});


// ── CONTACT FORM ──
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', function(e) {
    e.preventDefault();

    // Get values
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    // Simple validation
    if (!name || !email || !message) {
      alert('Please fill in all required fields.');
      return;
    }

    // Show success message
    const successMsg = document.getElementById('formSuccess');
    successMsg.style.display = 'block';

    // Reset form
    contactForm.reset();

    // Hide success message after 5 seconds
    setTimeout(() => {
      successMsg.style.display = 'none';
    }, 5000);
  });
}


// ── ACTIVE NAV LINK ──
const currentPage = window.location.pathname.split('/').pop();
document.querySelectorAll('.nav-links a').forEach(link => {
  if (link.getAttribute('href') === currentPage) {
    link.style.color = '#6c63ff';
    link.style.fontWeight = '700';
  }
});

// ── SHOW OTHER SERVICE FIELD ──
const serviceSelect = document.getElementById('service');
const otherServiceGroup = document.getElementById('otherServiceGroup');

if (serviceSelect) {
  serviceSelect.addEventListener('change', function() {
    if (this.value === 'other') {
      otherServiceGroup.style.display = 'block';
    } else {
      otherServiceGroup.style.display = 'none';
    }
  });
}