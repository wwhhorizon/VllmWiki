# vllm-project/vllm#36326: [Bug]: VLLM compatibility issue with NVIDIA RTX PRO 6000 Blackwell SE

| 字段 | 值 |
| --- | --- |
| Issue | [#36326](https://github.com/vllm-project/vllm/issues/36326) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM compatibility issue with NVIDIA RTX PRO 6000 Blackwell SE

### Issue 正文摘录

### 📚 The doc issue I have `NVIDIA RTX PRO 6000 Blackwell SE server.` on that i have one trained model. now i want to start inferencing on it but showing an error. Command i used is: ``` vllm serve --tensor-parallel-size 4 --gpu-memory-utilization 0.7 --max-model-len 2048 --max-num-batched-tokens 4096 --trust-remote-code --port 8004` ``` Same thing is working fine on `Nvidia H100` GPU. versions of CUDA and VLLM on both servers are same. `cuda` - 12.8 `vLLM` - 0.17.0 SM version is: H100 = 9 RTX PRO 6000 = 12 which i have checked with: ``` import torch torch.cuda.get_device_capability(0) ``` ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: VLLM compatibility issue with NVIDIA RTX PRO 6000 Blackwell SE documentation ### 📚 The doc issue I have `NVIDIA RTX PRO 6000 Blackwell SE server.` on that i have one trained model. now i want to start inferencing...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: SE server.` on that i have one trained model. now i want to start inferencing on it but showing an error. Command i used is: ``` vllm serve --tensor-parallel-size 4 --gpu-memory-utilization 0.7 --max-model-len 2048 --ma...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ve `NVIDIA RTX PRO 6000 Blackwell SE server.` on that i have one trained model. now i want to start inferencing on it but showing an error. Command i used is: ``` vllm serve --tensor-parallel-size 4 --gpu-memory-utiliza...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance distributed_parallel;frontend_api;hardware_porting;model_support cuda env...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
