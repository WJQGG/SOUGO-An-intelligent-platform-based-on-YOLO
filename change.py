import os
import os.path
from xml.etree.ElementTree import parse, Element
#批量修改xml中内容
def test():
    path = "./data/Annotations/" # xml文件所在的目录
    files = os.listdir(path)  # 遍历文件夹下所有文件名称
    for xmlFile in files:  # 对所有文件进行循环遍历处理
        path1 = "./data/Annotations/"+xmlFile #定位当前处理的文件的路径
        newStr = os.path.join(path, xmlFile)

        dom = parse(newStr)  # 获取xml文件中的参数
        root = dom.getroot()  # 获取数据结构

        for obj in root.iter('object'): # 获取object节点中的name子节点（此处如果要换成别的比如bndbox）
            name = obj.find('name').text # 获取相应的文本信息
            #  以下为自定义的修改规则，我这里把文本信息为[1]~[5]的内容改成lack，依次类推
            if name in ['[Chihuahua]']:
                new_name = 'lack'
            elif name in ['[6]','[7]','[8]','[9]','[10]']:
                new_name = 'black_point'
            elif name in ['[11]','[12]','[13]','[14]','[15]']:
                new_name = 'crack'
            else:
                new_name = 'lack'
            obj.find('name').text = new_name # 修改
        dom.write(path1, xml_declaration=True) # 保存到指定文件
        pass
if __name__ == '__main__':
    test()
