# vllm-project/vllm#22533: [Bug]: gpt-oss-20b flaky BadRequest 400

| 字段 | 值 |
| --- | --- |
| Issue | [#22533](https://github.com/vllm-project/vllm/issues/22533) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpt-oss-20b flaky BadRequest 400

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm running `gpt-oss-20b` (cached locally) with docker image `vllm/vllm-openai:gptoss` with ``` export CUDA_VISIBLE_DEVICES=7 ; VLLM_DO_NOT_TRACK=1 VLLM_DISABLE_COMPILE_CACHE=1 VLLM_HOST_IP=$(hostname -i) VLLM_PORT=29507 /usr/bin/python3 -m vllm.entrypoints.openai.api_server --model /model/tmprfd6mv51 --port 8800 --host 0.0.0.0 --api-key nokey --dtype bfloat16 --enable-log-requests --tensor-parallel-size 1 --gpu-memory-utilization 0.95 --trust_remote_code --enable-chunked-prefill --max-num-batched-tokens 2048 --max-num-seqs 256 --max-model-len 131072 --served-model-name model ``` I keep running into these 400s that don't seem to reference my input query. This is using the `/v1/responses` API. Here are some of the 400 errors I've seen: `BadRequestError: Error code: 400 - {'object': 'error', 'message': 'Unknown role: final', 'type': 'BadRequestError', 'param': None, 'code': 400}` `BadRequestError: Error code: 400 - {'object': 'error', 'message': 'Unknown channel: commentaryanalysis', 'type': 'BadRequestError', 'param': None, 'code': 400}` `BadRequestError: Error code: 400 - {'object': 'error', 'message': 'Unknown recipient: contain...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ### 🐛 Describe the bug I'm running `gpt-oss-20b` (cached locally) with docker image `vllm/vllm-openai:gptoss` with ``` export CUDA_VISIBLE_DEVICES=7 ; VLLM_DO_NOT_TRACK=1 VLLM_DISABLE_COMPILE_CACHE=1 VLLM_HOST_IP=$(host...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: /model/tmprfd6mv51 --port 8800 --host 0.0.0.0 --api-key nokey --dtype bfloat16 --enable-log-requests --tensor-parallel-size 1 --gpu-memory-utilization 0.95 --trust_remote_code --enable-chunked-prefill --max-num-batched-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: gpt-oss-20b flaky BadRequest 400 bug;stale ### Your current environment ### 🐛 Describe the bug I'm running `gpt-oss-20b` (cached locally) with docker image `vllm/vllm-openai:gptoss` with ``` export CUDA_VISIBLE_D...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed locally) with docker image `vllm/vllm-openai:gptoss` with ``` export CUDA_VISIBLE_DEVICES=7 ; VLLM_DO_NOT_TRACK=1 VLLM_DISABLE_COMPILE_CACHE=1 VLLM_HOST_IP=$(hostname -i) VLLM_PORT=29507 /usr/bin/python3 -m vllm.entr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: gpt-oss-20b flaky BadRequest 400 bug;stale ### Your current environment ### 🐛 Describe the bug I'm running `gpt-oss-20b` (cached locally) with docker image `vllm/vllm-openai:gptoss` with ``` export CUDA_VISIBLE_D...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
