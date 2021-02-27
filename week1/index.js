;(() => {
    const NAVIGATION = document.querySelector('.navigation-anime')
    for (let i = 0; i <= 100; i++) {
        const block = document.createElement('div')
        block.classList.add('anime-block')
        NAVIGATION.appendChild(block)
    }
    function animateCircles() {
        anime({
            targets: '.anime-block',
            translateX: () => anime.random(1200, -1200),
            translateY: () => anime.random(1200, -1200),
            scale: () => anime.random(1, 4),
            easing: 'linear',
            duration: 2000,
            opacity: 1,
            delay: anime.stagger(10),
            direction: 'alternate',
            complete: () => {
                opacity('.navigation-anime')
            },
        })
    }
    function opacity(className) {
        anime({
            targets: className,
            opacity: 0,
            duration: 2000,
            complete: () => {
                const div = document.querySelector(className)
                document.body.removeChild(div)
            },
        })
    }
    animateCircles()
})()
;(() => {
    const MENU = document.querySelector('.menu')
    const CLOSE = document.querySelector('.close')
    const MENULIST = document.querySelector('.menu-list')
    MENU.addEventListener('click', menuHandler)
    CLOSE.addEventListener('click', menuHandler)
    function menuHandler() {
        if (MENULIST.classList.contains('active')) {
            MENULIST.classList.remove('active')
        } else {
            MENULIST.classList.add('active')
        }
    }
})()
;(() => {
    const BANNER = document.querySelector('.banner > ul')
    const LI = document.querySelectorAll('.banner > ul li')
    const DOT = document.querySelector('.dot')
    const PREBUTTON = document.querySelector('.preButton')
    const NEXTBUTTON = document.querySelector('.nextButton')
    let DOTS = null
    let liCount = 0
    let index = 1
    let defaultLeft = 100
    let flag = false
    let timer = null
    let autoTime = 4000
    let moveTime = autoTime / 2
    carouselInit()
    NEXTBUTTON.addEventListener('click', () => {
        bannerHandler(1)
    })
    PREBUTTON.addEventListener('click', () => {
        bannerHandler(-1)
    })
    function timerHandler() {
        timer = setInterval(() => {
            flag = true
            index = index + 1
            BANNER.style.transition = 'left 2s'
            BANNER.style.left = -(defaultLeft * index) + 'vw'
            if (index === liCount - 1) {
                index = 1
                DOTS.forEach((item) => {
                    item.classList.remove('active')
                })
                setTimeout(() => {
                    BANNER.style.transition = '0s'
                    BANNER.style.left = -(index * defaultLeft) + 'vw'
                    DOTS[index - 1].classList.add('active')
                    flag = false
                }, moveTime)
                return
            }
            DOTS.forEach((item) => {
                item.classList.remove('active')
            })
            setTimeout(() => {
                DOTS[index - 1].classList.add('active')
                flag = false
            }, moveTime)
        }, autoTime)
    }
    function carouselInit() {
        for (let i = 0; i < LI.length; i++) {
            let li = document.createElement('li')
            li.innerHTML = 'o'
            li.setAttribute('index', i + 1)
            DOT.appendChild(li)
        }
        DOTS = document.querySelectorAll('.dot > li')
        BANNER.appendChild(LI[0].cloneNode(true))
        BANNER.prepend(LI[LI.length - 1].cloneNode(true))
        liCount = document.querySelectorAll('.banner > .content > li').length
        BANNER.style.width = 100 * liCount + 'vw'
        BANNER.style.left = -(defaultLeft * index) + 'vw'
        DOTS[index - 1].classList.add('active')
        timerHandler()
        DOTS.forEach((li) => {
            li.addEventListener('click', function () {
                if (flag) return
                clearInterval(timer)
                BANNER.style.transition = 'left 2s'
                flag = true
                let i = this.getAttribute('index')
                DOTS.forEach((item) => {
                    item.classList.remove('active')
                })
                DOTS[i - 1].classList.add('active')
                BANNER.style.left = -(i * defaultLeft) + 'vw'
                index = Number(i)
                setTimeout(() => {
                    flag = false
                }, moveTime)
                timerHandler()
            })
        })
    }
    function bannerHandler(num) {
        let type = num > 0 ? true : false
        if (flag) return
        clearInterval(timer)
        flag = true
        if (type) index = index + 1
        if (!type) index = index - 1
        BANNER.style.transition = 'left 2s'
        BANNER.style.left = -(defaultLeft * index) + 'vw'
        DOTS.forEach((item) => {
            item.classList.remove('active')
        })
        timerHandler()
        if (index === liCount - 1 && flag) {
            setTimeout(() => {
                index = 1
                BANNER.style.transition = '0s'
                BANNER.style.left = -(index * defaultLeft) + 'vw'
                DOTS[index - 1].classList.add('active')
                flag = false
            }, moveTime)
            return
        }
        if (index === 0 && !flag) {
            setTimeout(() => {
                index = liCount - 2
                BANNER.style.transition = '0s'
                BANNER.style.left = -(index * defaultLeft) + 'vw'
                DOTS[index - 1].classList.add('active')
                flag = false
            }, moveTime)
            return
        }
        setTimeout(() => {
            flag = false
            DOTS[index - 1].classList.add('active')
        }, moveTime)
    }
})()
