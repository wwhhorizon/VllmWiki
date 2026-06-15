# vllm-project/vllm#10115: [Doc]: follow the doc but got error

| 字段 | 值 |
| --- | --- |
| Issue | [#10115](https://github.com/vllm-project/vllm/issues/10115) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: follow the doc but got error

### Issue 正文摘录

### 📚 The doc issue i have cuda11.8 python==3.10.15, and follow the https://docs.vllm.ai/en/latest/getting_started/installation.html get the code export VLLM_VERSION=0.6.1.post1 export PYTHON_VERSION=310 pip install https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cu118-cp${PYTHON_VERSION}-cp${PYTHON_VERSION}-manylinux1_x86_64.whl --extra-index-url https://download.pytorch.org/whl/cu118 after installed , i found the torch is 12.1. it totally different with the what the doc said. ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ==3.10.15, and follow the https://docs.vllm.ai/en/latest/getting_started/installation.html get the code export VLLM_VERSION=0.6.1.post1 export PYTHON_VERSION=310 pip install https://github.com/vllm-project/vllm/releases...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : follow the doc but got error documentation ### 📚 The doc issue i have cuda11.8 python==3.10.15, and follow the https://docs.vllm.ai/en/latest/getting_started/installation.html get the code export VLLM_VERSION=0.6.1.po...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: have cuda11.8 python==3.10.15, and follow the https://docs.vllm.ai/en/latest/getting_started/installation.html get the code export VLLM_VERSION=0.6.1.post1 export PYTHON_VERSION=310 pip install https://github.com/vllm-p...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
