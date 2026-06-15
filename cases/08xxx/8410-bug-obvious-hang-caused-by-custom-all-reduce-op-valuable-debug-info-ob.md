# vllm-project/vllm#8410: [Bug]: Obvious hang caused by Custom All Reduce OP（Valuable Debug Info Obtained）

| 字段 | 值 |
| --- | --- |
| Issue | [#8410](https://github.com/vllm-project/vllm/issues/8410) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Obvious hang caused by Custom All Reduce OP（Valuable Debug Info Obtained）

### Issue 正文摘录

### Your current environment ### Model Input Dumps Not available at the moment. ### 🐛 Describe the bug The problem I encountered was "NCCL hangs and causes timeout", which is similar to https://github.com/vllm-project/vllm/issues/5484 Before debugging, I have read https://docs.vllm.ai/en/latest/getting_started/debugging.html ，and add additional log in https://github.com/vllm-project/vllm/blob/7de49aa86c7f169eb0962b6db29ad53fff519ffb/vllm/_custom_ops.py#L825-L827 Here is the service launch code for debugging ` CUDA_LAUNCH_BLOCKING=1 python3 -m vllm.entrypoints.openai.api_server --served-model-name Qwen2-72B-Instrust --model /data/Qwen2-72B-Instruct --tensor-parallel-size 8 --port 8000 --max_model_len 4096 --trust-remote-code --max_num_seqs 32 --dytpe bfloat16 --enforce-eager ` When the hang occurs, I see an obvious phenomenon, as shown in the picture below： ![1726142733383](https://github.com/user-attachments/assets/8f60b020-b87a-4c09-bee4-d646e9185218) （1）Obviously, the root cause is that RANK2 is hanged. In my opinion they should end communication at the same time and print a log, when ‘CUDA_LAUNCH_BLOCKING=1’ was added. （2）‘--disable_custom_all_reduce’ seem to work. （3）This bug...

## 现有链接修复摘要

#8558 [Bugfix] Fix potentially unsafe custom allreduce synchronization

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ）‘--disable_custom_all_reduce’ seem to work. （3）This bug appears in both version 0.5.4 and version 0.6.0. I'd be happy to take more debugging guidance from you and provide more debugging information. ### Before submitti...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 8000 --max_model_len 4096 --trust-remote-code --max_num_seqs 32 --dytpe bfloat16 --enforce-eager ` When the hang occurs, I see an obvious phenomenon, as shown in the picture below： ![1726142733383](https://github.com/us...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: P（Valuable Debug Info Obtained） bug ### Your current environment ### Model Input Dumps Not available at the moment. ### 🐛 Describe the bug The problem I encountered was "NCCL hangs and causes timeout", which is similar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: custom_ops.py#L825-L827 Here is the service launch code for debugging ` CUDA_LAUNCH_BLOCKING=1 python3 -m vllm.entrypoints.openai.api_server --served-model-name Qwen2-72B-Instrust --model /data/Qwen2-72B-Instruct --tens...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error dtype;env_dependency #8558 [Bugfix] Fix potentially unsafe custom allreduce synchronization Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8558](https://github.com/vllm-project/vllm/pull/8558) | closes_keyword | 0.95 | [Bugfix] Fix potentially unsafe custom allreduce synchronization | FIX #8410 #8404 Use incrementing counter as discussed, but two sets of counter is needed. Also, we avoid incrementing peer counters to avoid round trip latency. Instead, we incr |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
