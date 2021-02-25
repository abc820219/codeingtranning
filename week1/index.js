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
    DOTS.forEach((li) => {
        li.addEventListener('click', function () {
            if (flag) return
            BANNER.style.transition = 'left 1s'
            flag = true
            let i = this.getAttribute('index')
            DOTS.forEach((item) => {
                item.classList.remove('active')
            })
            DOTS[i - 1].classList.add('active')
            BANNER.style.left = -(i * defaultLeft) + 'vw'
            console.log(i)
            index = Number(i)
            setTimeout(() => {
                flag = false
            }, 1000)
        })
    })
    NEXTBUTTON.addEventListener('click', () => {
        if (flag) return
        flag = true
        index = index + 1
        BANNER.style.transition = 'left 1s'
        BANNER.style.left = -(defaultLeft * index) + 'vw'
        DOTS.forEach((item) => {
            item.classList.remove('active')
        })
        if (index === liCount - 1) {
            setTimeout(() => {
                index = 1
                BANNER.style.transition = '0s'
                BANNER.style.left = -(index * defaultLeft) + 'vw'
                DOTS[index - 1].classList.add('active')
                flag = false
            }, 1000)
            return
        }
        setTimeout(() => {
            flag = false
            DOTS[index - 1].classList.add('active')
        }, 1000)
    })
    PREBUTTON.addEventListener('click', () => {
        console.log(flag)
        if (flag) return
        flag = true
        index = index - 1
        BANNER.style.transition = 'left 1s'
        BANNER.style.left = -(defaultLeft * index) + 'vw'
        DOTS.forEach((item) => {
            item.classList.remove('active')
        })
        if (index === 0) {
            setTimeout(() => {
                index = liCount - 2
                BANNER.style.transition = '0s'
                BANNER.style.left = -(index * defaultLeft) + 'vw'
                DOTS[index - 1].classList.add('active')
                flag = false
            }, 1000)
            return
        }
        setTimeout(() => {
            flag = false
            DOTS[index - 1].classList.add('active')
        }, 1000)
    })
})()
