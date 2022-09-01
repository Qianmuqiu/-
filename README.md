训练：
激活函数
反向传播，loss以及梯度的计算

学习率下降策略
L2正则化
优化器SGD
保存模型

参数查找：学习率，隐藏层大小，正则化强度
测试：导入模型，用经过参数查找后的模型进行测试，输出分类精度

学习率查找范围为[5e-3, 1e-2, 2e-2]，隐藏层大小查找范围为[20, 30, 40]，正则化强度查找范围为[0, 1e-2, 2e-2]

训练方式：激活函数：activations.py
         反向传播，loss以及梯度的计算：model.backward方法
         学习率下降策略：optimizer.py
         L2正则化：采用weight_dacay进行实现，optimizer.step
         优化器SGD：optimizer.py
         保存模型：model.save
         训练主函数为utils.fit，训练记录在logs文件夹中
         
测试方式：导入模型，用经过参数查找后的模型进行测试，输出分类精度
