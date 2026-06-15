# vllm-project/vllm#27782: [Usage]: The same configuration v0.11.0 will report insufficient video memory compared to v0.8.5

| 字段 | 值 |
| --- | --- |
| Issue | [#27782](https://github.com/vllm-project/vllm/issues/27782) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | crash;oom |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: The same configuration v0.11.0 will report insufficient video memory compared to v0.8.5

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm The server is a 4090 with 4 cards Docker runs vllm openai: v0.8.5 deployment command: "command: --model /models/Qwen3/Qwen3-30B-A3B --enable-reasoning --reasoning-parser deepseek_r1 --tensor_parallel_size 4" Can be deployed and started normally, switch the image version to v0.11.0, and run the command "command: --model /models/Qwen3/Qwen3-30B-A3B --reasoning-parser deepseek_r1 --tensor_parallel_size 4" It will report that the graphics card memory is insufficient, and the error log is: Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|██████████| 67/67 [00:19<00:00, 3.43it/s] Capturing CUDA graphs (decode, FULL): 100%|██████████| 35/35 [00:07<00:00, 4.78it/s] vllm | (Worker_TP3 pid=263) INFO 10-29 19:57:20 [gpu_model_runner.py:3480] Graph capturing finished in 28 secs, took 1.88 GiB vllm | (Worker_TP1 pid=261) INFO 10-29 19:57:20 [gpu_model_runner.py:3480] Graph capturing finished in 28 secs, took 1.88 GiB vllm | (Worker_TP0 pid=260) INFO 10-29 19:57:20 [gpu_model_runner.py:3480] Graph capturing finished in 28 secs, took 1.88 GiB vllm | (Worker_TP2 pid=262)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Usage]: The same configuration v0.11.0 will report insufficient video memory compared to v0.8.5 usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: n v0.11.0 will report insufficient video memory compared to v0.8.5 usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm The server is a 4090 with...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: r.py:671] sampled, processed_logprobs = self.sample(logits, sampling_metadata) vllm | (Worker_TP2 pid=262) ERROR 10-29 19:57:21 [multiproc_executor.py:671] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ vllm | (Worker_TP2 pid=2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: The same configuration v0.11.0 will report insufficient video memory compared to v0.8.5 usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: he graphics card memory is insufficient, and the error log is: Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|██████████| 67/67 [00:19<00:00, 3.43it/s] Capturing CUDA graphs (decode, FULL): 100%|█████████...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
