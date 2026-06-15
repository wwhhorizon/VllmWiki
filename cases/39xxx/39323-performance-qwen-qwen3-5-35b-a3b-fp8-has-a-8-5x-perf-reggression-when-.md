# vllm-project/vllm#39323: [Performance]: Qwen/Qwen3.5-35B-A3B-FP8 has a 8.5x perf reggression when using FA3 backend on a Hopper backend

| 字段 | 值 |
| --- | --- |
| Issue | [#39323](https://github.com/vllm-project/vllm/issues/39323) |
| 状态 | open |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Qwen/Qwen3.5-35B-A3B-FP8 has a 8.5x perf reggression when using FA3 backend on a Hopper backend

### Issue 正文摘录

### Proposal to improve performance There are 2 solutions to this: 1) Update the FA3 backend codebase (which is where the bug is) 2) Make FLASHINFER the default choice of attention backend for Hopper GPUs (1) has already been done in the latest nightly build. The nightly no longer has this performance bug, but I wanted to raise it incase existing users running with vLLM 0.19.0 have issues. (2) I've found that in general the FLASHINFER kernels are as perofrmance of FLASHATTN and is also the default for Blackwell. So maybe making this default for Hopper is also a good idea. ### Report of performance regression On a 1xH100 machine, I launched vLLM with two configurations: Config 1) `vllm serve Qwen/Qwen3.5-35B-A3B-FP8 --host 0.0.0.0 --port 8000` Config 2) `vllm serve Qwen/Qwen3.5-35B-A3B-FP8 --host 0.0.0.0 --port 8000 --attention-backend FLASHINFER` I then ran the following benchmark: ``` vllm bench serve --backend vllm --base-url http://localhost:8000 --model Qwen/Qwen3.5-35B-A3B-FP8 --endpoint /v1/completions --dataset-name random --random-input-len 4096 --random-output-len 256 --num-prompts 256 --num-warmups 10 --request-rate inf --ignore-eos ``` The results were as follows: | Met...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: of attention backend for Hopper GPUs (1) has already been done in the latest nightly build. The nightly no longer has this performance bug, but I wanted to raise it incase existing users running with vLLM 0.19.0 have is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: n3.5-35B-A3B-FP8 has a 8.5x perf reggression when using FA3 backend on a Hopper backend performance ### Proposal to improve performance There are 2 solutions to this: 1) Update the FA3 backend codebase (which is where t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: rmance]: Qwen/Qwen3.5-35B-A3B-FP8 has a 8.5x perf reggression when using FA3 backend on a Hopper backend performance ### Proposal to improve performance There are 2 solutions to this: 1) Update the FA3 backend codebase...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: Qwen/Qwen3.5-35B-A3B-FP8 has a 8.5x perf reggression when using FA3 backend on a Hopper backend performance ### Proposal to improve performance There are 2 solutions to this: 1) Update the FA3 backend cod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: backend for Hopper GPUs (1) has already been done in the latest nightly build. The nightly no longer has this performance bug, but I wanted to raise it incase existing users running with vLLM 0.19.0 have issues. (2) I'v...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
