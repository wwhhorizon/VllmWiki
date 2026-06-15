# vllm-project/vllm#10924: [Bug]: Not able to install/compile vllm using alpine linux base image

| 字段 | 值 |
| --- | --- |
| Issue | [#10924](https://github.com/vllm-project/vllm/issues/10924) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Not able to install/compile vllm using alpine linux base image

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Not able to compile/ install vllm using an alpine linux based image. Does vllm support? RUN pip install --upgrade pip RUN pip install Pillow==8.2.0 numpy wheel packaging ninja "setuptools>=49.4.0" RUN git clone https://github.com/vllm-project/vllm.git && cd vllm && \ pip install -v -r requirements-cpu.txt --extra-index-url https://download.pytorch.org/whl/cpu RUN VLLM_TARGET_DEVICE=cpu python setup.py install ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Not able to install/compile vllm using alpine linux base image bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Not able to compile/ install vllm using an alpine l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: all ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: g alpine linux base image bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Not able to compile/ install vllm using an alpine linux based image. Does vllm support? RUN pip...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Bug]: Not able to install/compile vllm using alpine linux base image bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Not able to compile/ install vllm using an alpine li...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
