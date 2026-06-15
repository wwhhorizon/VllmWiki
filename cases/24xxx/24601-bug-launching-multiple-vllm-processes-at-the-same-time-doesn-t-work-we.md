# vllm-project/vllm#24601: [Bug]: Launching multiple vLLM processes at the same time doesn't work well with vLLM's compile cache

| 字段 | 值 |
| --- | --- |
| Issue | [#24601](https://github.com/vllm-project/vllm/issues/24601) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 28; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Launching multiple vLLM processes at the same time doesn't work well with vLLM's compile cache

### Issue 正文摘录

### Your current environment My makefile: ``` clean: rm -rf /tmp/torchinductor_rzou rm -rf ~/.cache/vllm/torch_compile_cache killall -9 "VLLM::EngineCore" run: VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=2 vllm serve --gpu-memory-utilization 0.1 & VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=3 vllm serve --gpu-memory-utilization 0.1 & VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=4 vllm serve --gpu-memory-utilization 0.1 & VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=5 vllm serve --gpu-memory-utilization 0.1 & VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=6 vllm serve --gpu-memory-utilization 0.1 & VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=7 vllm serve --gpu-memory-utilization 0.1 & ``` `make run` ### 🐛 Describe the bug The problem is: - we launch vllm in multiple processes - each process tries to compile and save an artifact to disk in the same location - each artifact is a directory - the directories get clobbered There's multiple ways I think we can fix the problem. I've tried some of these and haven't gotten them to work yet. - standalone_compile offers a "binary" option instead of a "directory" option. writing to these b...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: illall -9 "VLLM::EngineCore" run: VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=2 vllm serve --gpu-memory-utilization 0.1 & VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=3 vllm serve --gpu-memory-utiliza...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: g multiple vLLM processes at the same time doesn't work well with vLLM's compile cache bug;torch.compile ### Your current environment My makefile: ``` clean: rm -rf /tmp/torchinductor_rzou rm -rf ~/.cache/vllm/torch_com...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
