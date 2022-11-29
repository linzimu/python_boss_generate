def static_resource_deal(src_filepath="./超市数据可视化大屏.html", dst_filepath="./test.html"):
    with open(src_filepath, "r", encoding="utf8") as fr, open(dst_filepath, "w", encoding="utf8") as fw:
        for line in fr:
            if "echarts.min.js" in line:
                with open("./external_resources/echarts.min.js") as f_replace1:
                    replace1 = f'<script type="text/javascript">{f_replace1.read()}</script>'
                fw.write(replace1)
            elif "jquery.min.js" in line:
                with open("./external_resources/jquery.min.js") as f_replace2:
                    replace2 = f'<script type="text/javascript">{f_replace2.read()}</script>'
                fw.write(replace2)
            elif "jquery-ui.css" in line:
                with open("./external_resources/jquery-ui.css") as f_replace3:
                    replace3 = f'<style type="text/css">{f_replace3.read()}</style>'
                fw.write(replace3)
            elif "jquery-ui.min.js" in line:
                with open("./external_resources/jquery-ui.min.js") as f_replace4:
                    replace4 = f'<script type="text/javascript">{f_replace4.read()}</script>'
                fw.write(replace4)
            elif "ResizeSensor.js" in line:
                with open("./external_resources/ResizeSensor.js") as f_replace5:
                    replace5 = f'<script type="text/javascript">{f_replace5.read()}</script>'
                fw.write(replace5)
            elif "USA.js" in line:
                with open("./external_resources/USA.js") as f_replace6:
                    replace6 = f'<script type="text/javascript">{f_replace6.read()}</script>'
                fw.write(replace6)
            else:
                fw.writelines(line)


if __name__ == '__main__':
    static_resource_deal(dst_filepath="调整布局.html")
