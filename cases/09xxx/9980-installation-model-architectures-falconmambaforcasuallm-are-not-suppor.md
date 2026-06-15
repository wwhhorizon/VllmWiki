# vllm-project/vllm#9980: [Installation]: Model Architectures FalconMambaForCasualLM are not supported for now.  

| 字段 | 值 |
| --- | --- |
| Issue | [#9980](https://github.com/vllm-project/vllm/issues/9980) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Model Architectures FalconMambaForCasualLM are not supported for now.  

### Issue 正文摘录

### Your current environment The model (tiiuae/falcon-mamba-7b-instruct) is downloaded and getting error while starting the instance. ![image](https://github.com/user-attachments/assets/6a8033b9-e188-404c-a6b3-db362b13abe2) ### How you are installing vllm I tried to deploy falcon-mamba-7b-instruct (tiiuae/falcon-mamba-7b-instruct)model from huggingace by using VLLM. But unfortunately i get an error like model architectures are not available now. Then, I ran tiiuae/falcon-7b-instruct model, and it is working fine without any errors. But, I want to run the tiiuae/falcon-mamba-7b-instructmodel without any errors. How can I fix this? Do I need to change any versions of the VLLM. I already tried with the latest and some other versions. Is there any specific version to use? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: Model Architectures FalconMambaForCasualLM are not supported for now. installation ### Your current environment The model (tiiuae/falcon-mamba-7b-instruct) is downloaded and getting error while starting
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Installation]: Model Architectures FalconMambaForCasualLM are not supported for now. installation ### Your current environment The model (tiiuae/falcon-mamba-7b-instruct) is downloaded and getting error while starting...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Installation]: Model Architectures FalconMambaForCasualLM are not supported for now. installation ### Your current environment The model (tiiuae/falcon-mamba-7b-instruct) is downloaded and getting error while starting...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Do I need to change any versions of the VLLM. I already tried with the latest and some other versions. Is there any specific version to use? ### Before submitting a new issue... - [X] Make sure you already searched for...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
