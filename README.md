# 《深度学习理论与应用》案例复现

本项目为《深度学习理论与应用》一书中的深度学习案例代码复现与实践。通过完成这些案例，我系统性地学习了深度学习模型的构建、训练、可视化与调试。

---

## 项目资源说明

由于GitHub对文件大小限制，本仓库仅包含代码文件。**完整的项目资源（包括代码、数据集、预训练模型）** 均存储在夸克网盘中。

**🔗 完整资源下载地址：** [https://pan.quark.cn/s/c61487f55d39](https://pan.quark.cn/s/c61487f55d39)

> **请注意**：从夸克网盘下载完整项目后，配置好环境即可直接运行所有案例，无需从本GitHub仓库单独下载代码。

---

## 运行环境

本项目在多种硬件环境下完成，各章节运行环境如下：

### 本地环境 (Windows)

- **GPU:** NVIDIA MX450
- **CUDA:** 11.3
- **Python:** 3.8
- **PyTorch:** 1.12.0
- **主要用于运行：** 第1-4章案例

### 服务器环境 1 (Linux)

- **GPU:** NVIDIA RTX 2080 Ti (11GB)
- **CUDA:** 11.3.0
- **Python:** 3.8
- **PyTorch:** 1.12.1

### 服务器环境 2 (Linux)

- **GPU:** NVIDIA RTX 3060 (12GB)
- **CUDA:** 11.3
- **Python:** 3.8
- **PyTorch:** 1.12.1

### 服务器环境 3 (Linux)

- **GPU:** NVIDIA RTX 2080 Ti (11GB)
- **CUDA:** 12.1.1
- **Python:** 3.11
- **PyTorch:** 2.2.1
- **服务器环境1-3主要用于运行：** 第5-10章大部分案例

---

## 快速开始 (本地Windows环境)

如果你想在本地Windows环境下运行代码，请按以下步骤操作：

1. **下载完整资源**

   ```bash
   # 从夸克网盘下载并解压完整资源包，其中已包含代码、数据和模型。
   ```

2. **创建并激活Conda环境（推荐）**

   ```bash
   # 创建Python 3.8环境
   conda create -n pytorch1 python=3.8 -y
   conda activate pytorch1
   ```

3. **安装PyTorch (CUDA 11.3版本)**
   请根据你的CUDA版本从[PyTorch官网](https://pytorch.org/get-started/previous-versions/)获取准确的安装命令。例如：

   ```bash
   # 适用于CUDA 11.3的PyTorch 1.12.0
   pip install torch==1.12.0+cu113 torchvision==0.13.0+cu113 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu113
   ```

4. **安装其他项目依赖**

   ```bash
   # 进入项目根目录，安装requirements.txt中列出的包（夸克网盘没有requirements.txt文件，需从该库中下载）
   pip install -r requirements.txt
   ```

5. **运行案例**
   现在你可以运行任意章节的代码了，例如：

   ```bash
   python chapter_2/ex_2.1.py
   ```

---

## 重要提示与说明

1.  **操作系统兼容性**：
    - 夸克网盘中的完整代码是为 **Windows系统** 配置的路径。
    - 如果你需要在 **Linux服务器** 上运行夸克网盘中的代码，请注意修改文件路径（如将 `D:\\data` 改为 `/home/user/data`）。
2.  **运行结果与服务器代码**：
    - 在 `results/` 文件夹中，你可以找到第5、6、7、8、10章案例的运行结果。
    - 同时，`results/` 中也提供了**已在Linux服务器上适配好的代码版本**(有些案例忘记保存Linux代码)，可直接在服务器环境运行。
3.  **服务器租赁与使用教程**：
    - 对于需要租用云服务器来完成大算力需求的同学，我在 `results/` 文件夹中附上了详细的**服务器租赁教程**（智星云和恒源云）和**本地数据上传到服务器的教程**。

---

## 总结

通过复现本书所有案例，我深入学习了：

- 深度学习模型的整体框架与搭建
- 模型训练、调试与可视化
- 在不同硬件环境（本地/服务器）下的项目部署与迁移
- 解决实际问题的工程化能力

希望本项目能对你的学习有所帮助！
