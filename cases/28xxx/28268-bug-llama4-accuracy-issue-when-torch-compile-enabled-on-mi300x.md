# vllm-project/vllm#28268: [Bug]: Llama4 accuracy issue when torch.compile enabled on MI300x

| 字段 | 值 |
| --- | --- |
| Issue | [#28268](https://github.com/vllm-project/vllm/issues/28268) |
| 状态 | closed |
| 标签 | bug;rocm;torch.compile;stale |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;fp8;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama4 accuracy issue when torch.compile enabled on MI300x

### Issue 正文摘录

### Your current environment torch version: 2.8.0+rocm6.4 hardware: mi300x ### 🐛 Describe the bug Run: ``` vllm serve meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 -tp 8 --max-num-seqs 64 ``` Run gsm8k eval: ``` lm_eval --model local-completions --tasks gsm8k --model_args model=meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8,base_url=http://127.0.0.1:8000/v1/completions,num_concurrent=64 --batch_size auto --limit 200 ``` Score is 0: ``` |Tasks|Version| Filter |n-shot| Metric | |Value| |Stderr| |-----|------:|----------------|-----:|-----------|---|----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ | 0|± | 0| | | |strict-match | 5|exact_match|↑ | 0|± | 0| ``` Disable CUDAGraph only with `--compilation-config '{"cudagraph_mode":0}' `, score is still 0 Disable compile with `--enforce-eager` and run eval: ``` |Tasks|Version| Filter |n-shot| Metric | |Value| |Stderr| |-----|------:|----------------|-----:|-----------|---|----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ | 0.93|± |0.0256| | | |strict-match | 5|exact_match|↑ | 0.92|± |0.0273| ``` Tested with `Qwen/Qwen3-8B` and it is OK: ``` |Tasks|Version| Filter |n-shot| Metric | |Value| |Stderr| |-----|---...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: Llama4 accuracy issue when torch.compile enabled on MI300x bug;rocm;torch.compile;stale ### Your current environment torch version: 2.8.0+rocm6.4 hardware: mi300x ### 🐛 Describe the bug Run: ``` vllm serve meta-l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Llama4 accuracy issue when torch.compile enabled on MI300x bug;rocm;torch.compile;stale ### Your current environment torch version: 2.8.0+rocm6.4 hardware: mi300x ### 🐛 Describe the bug Run: ``` vllm serve meta-l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Llama4 accuracy issue when torch.compile enabled on MI300x bug;rocm;torch.compile;stale ### Your current environment torch version: 2.8.0+rocm6.4 hardware: mi300x ### 🐛 Describe the bug Run: ``` vllm serve meta-l...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: Happens on AMD (MI300x) but not on NVIDIA (H100). Issue exists on both Triton Attention (default) and AITER MHA attention backends (`VLLM_ROCM_USE_AITER_MHA=1 VLLM_ROCM_USE_AITER=1`) for AMD ### Before submitting a new...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e bug Run: ``` vllm serve meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 -tp 8 --max-num-seqs 64 ``` Run gsm8k eval: ``` lm_eval --model local-completions --tasks gsm8k --model_args model=meta-llama/Llama-4-Maverick-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
