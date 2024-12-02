import numpy as np
import matplotlib.pyplot as plt


def trf(x, t, v):
    g = 1/np.sqrt(1-v**2)
    return g*(x-v*t), g*(t-v*x)


def trace_lu(v=0.6, x=9, td=7, tf=11):
    N = 10
    event_x = np.array([x, x])
    event_t = np.array([td, tf])
    x = np.linspace(0, N, N+1)
    t = np.linspace(0, N, N+1)
    plt.figure(figsize=(8, 8))
    for n in range(N+1):
        plt.plot(*trf(np.array([x[n], x[n]]),
                 np.array([0, t[-1]]), -v), 'b', lw=0.25)
    for n in range(N+1):
        plt.plot(*trf(np.array([0, x[-1]]),
                 np.array([t[n], t[n]]), -v), 'b', lw=0.25)
    xo, to = trf(event_x, event_t, v)
    plt.plot(event_x, event_t, 'r', lw=1.5,
             label=f'$\Delta t=${event_t[1]-event_t[0]:.4f}')
    plt.plot(*trf(xo, np.array([0, 0]), -v), 'k',
             lw=1, label=f'$\Delta x\'=${xo[1]-xo[0]:.4f}')
    plt.plot(*trf(np.array([0, 0]), to, -v), 'g', lw=1,
             label=f'$\Delta t\'=${to[1]-to[0]:.4f}')

    plt.grid('on')
    MAX = trf(N, N, -v)[0]
    plt.xticks(np.arange(0, MAX+1, 1))
    plt.yticks(np.arange(0, MAX+1, 1))
    plt.xlabel('$x$')
    plt.ylabel('$t$')
    plt.axis('equal')
    plt.title(f'$v=${v:.4f}, $\gamma=${1/np.sqrt(1-v**2):.4f}')
    plt.legend()
    print('\n***Résultats***')
    print(f'L ={v*(event_t[1]-event_t[0]):.4f}')
    print(f'L\'={xo[0]-xo[1]:.4f}')
    print('\n***Tracé***')
    plt.show()
