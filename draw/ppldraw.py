import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def pplnum_drawbar(pplnum,name):
    matplotlib.use('TkAgg')
    n=len(pplnum)
    x=[2,4,6,8,10,12,14,16]#ȷ����״ͼ����,������Ϊ��x����̶�

    y=pplnum#y����̶�

    color=['green','yellow','orange','brown','red','purple','blue','black']
    x_label=['0-10','10-25','25-50','50-100','100-500','500-1000','1000-2000','>2000']
    # plt.xticks(x, x_label)#����x�̶ȱ�ǩ
    # plt.bar(x, y,width=[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],bottom=0,color=color)#����y�̶ȱ�ǩ
    # plt.legend()
    # plt.grid(True, linestyle=':', color='r', alpha=0.6)
    # plt.show()

    fig, ax = plt.subplots(dpi=200,figsize=(30,10))
    ax.bar(x, y,color=color)
    ax.set_xticks(x)
    ax.set_xticklabels(x_label)
    plt.tick_params(labelsize=25)
    # plt.xlabel(labelpad=0.5)
    # width=0.2
    # x_major_locator = MultipleLocator(1)
    # ax.xaxis.set_major_locator(x_major_locator)
    # ax.set_xlim([-0.5, 2.5])
    plt.title(name,fontproperties="STSong",fontsize=40)

    figpath='D:\PyProject\docx_input\data_cache\ppl_distribution_figure'
    plt.savefig(figpath+'\\'+name+'.png')
    # plt.show()

    #��������̶�
