# vllm-project/vllm#36327: [Bug]: Compatibility issue NVIDIA RTX PRO 6000 Blackwell SE

| 字段 | 值 |
| --- | --- |
| Issue | [#36327](https://github.com/vllm-project/vllm/issues/36327) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Compatibility issue NVIDIA RTX PRO 6000 Blackwell SE

### Issue 正文摘录

### Your current environment GPU : - Nvidia RTX PRO 6000 Blackwell edition - H100 - Virtual environment Created - vll installed with `pip install vllm` - versions of CUDA and VLLM on both servers are same. `cuda` - 12.8 `vLLM` - 0.17.0 - SM version is: H100 = 9 RTX PRO 6000 = 12 ### 🐛 Describe the bug I have `NVIDIA RTX PRO 6000 Blackwell SE server.` on that i have one trained model. now i want to start inferencing on it but showing an error. Command i used is: ``` vllm serve --tensor-parallel-size 4 --gpu-memory-utilization 0.7 --max-model-len 2048 --max-num-batched-tokens 4096 --trust-remote-code --port 8004` ``` Same thing is working fine on `Nvidia H100` GPU. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Compatibility issue NVIDIA RTX PRO 6000 Blackwell SE bug ### Your current environment GPU : - Nvidia RTX PRO 6000 Blackwell edition - H100 - Virtual environment Created - vll installed with `pip install vllm` - v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: X PRO 6000 Blackwell edition - H100 - Virtual environment Created - vll installed with `pip install vllm` - versions of CUDA and VLLM on both servers are same. `cuda` - 12.8 `vLLM` - 0.17.0 - SM version is: H100 = 9 RTX...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ve `NVIDIA RTX PRO 6000 Blackwell SE server.` on that i have one trained model. now i want to start inferencing on it but showing an error. Command i used is: ``` vllm serve --tensor-parallel-size 4 --gpu-memory-utiliza...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
