# vllm-project/vllm#19828: [Usage]: vllm启动qwen2.5vl-7b以后 为什么显存使用越来越多

| 字段 | 值 |
| --- | --- |
| Issue | [#19828](https://github.com/vllm-project/vllm/issues/19828) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm启动qwen2.5vl-7b以后 为什么显存使用越来越多

### Issue 正文摘录

### Your current environment 使用vllm0.7.3启动qwen2.5vl-7b模型，模型启动命令是：nohup env CUDA_VISIBLE_DEVICES=4, vllm serve /Qwen/Qwen2___5-VL-7B-Instruct/ --trust-remote-code --served-model-name qwen_model --gpu-memory-utilization 0.9 --tensor-parallel-size 4 --port 8000 &>qwen.log & 使用显卡是4张nvidia 4090 最开始启动的时候显存占用是每张卡约8G左右，运行时间越长，显存占用越多，一晚上的显存占用增加到约12G左右。 ![Image](https://github.com/user-attachments/assets/b4083856-9935-4362-9a64-58436ac11107) ![Image](https://github.com/user-attachments/assets/23c7b6ba-4db7-4c16-b195-3973ea78771f) 请问为什么显存会越来越多呀？应该怎么解决这个问题呀？ ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. 我应该怎么使用vllm才不会造成这种显存越来越多的现象呢？ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 呀？ ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. 我应该怎么使用vllm才不会造成这种显存越来越多的现象呢？ ### Before submitting a new issue... - [x] Ma...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Your current environment 使用vllm0.7.3启动qwen2.5vl-7b模型，模型启动命令是：nohup env CUDA_VISIBLE_DEVICES=4, vllm serve /Qwen/Qwen2___5-VL-7B-Instruct/ --trust-remote-code --served-model-name qwen_model --gpu-memory-utilization 0.9 -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: vllm启动qwen2.5vl-7b以后 为什么显存使用越来越多 usage;stale ### Your current environment 使用vllm0.7.3启动qwen2.5vl-7b模型，模型启动命令是：nohup env CUDA_VISIBLE_DEVICES=4, vllm serve /Qwen/Qwen2___5-VL-7B-Instruct/ --trust-remote-code --s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: vllm启动qwen2.5vl-7b以后 为什么显存使用越来越多 usage;stale ### Your current environment 使用vllm0.7.3启动qwen2.5vl-7b模型，模型启动命令是：nohup env CUDA_VISIBLE_DEVICES=4, vllm serve /Qwen/Qwen2___5-VL-7B-Instruct/ --trust-remote-code --s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
