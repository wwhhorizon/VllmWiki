# vllm-project/vllm#8494: [Bug]: L40 GPU deepseek-v2 fp8  cuda graph error;  Using `--enforce-eager` can run properly.

| 字段 | 值 |
| --- | --- |
| Issue | [#8494](https://github.com/vllm-project/vllm/issues/8494) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: L40 GPU deepseek-v2 fp8  cuda graph error;  Using `--enforce-eager` can run properly.

### Issue 正文摘录

### Your current environment ### Model Input Dumps python3 -m vllm.entrypoints.openai.api_server --model neuralmagic/DeepSeek-Coder-V2-Instruct-FP8 --served-model-name dsv2 --trust-remote-code --tensor-parallel-size 8 --max-model-len 8192 --port $PORT0 --gpu-memory-utilization 0.99 --kv-cache-dtype fp8 >> deepseek_v2.log 2>&1 ### 🐛 Describe the bug Process SpawnProcess-1: Traceback (most recent call last): File "/home/tiger/.pyenv/versions/3.11.2/lib/python3.11/site-packages/vllm/worker/model_runner.py", line 1679, in capture output_hidden_or_intermediate_states = self.model( ^^^^^^^^^^^ File "/home/tiger/.pyenv/versions/3.11.2/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl return self._call_impl(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/tiger/.pyenv/versions/3.11.2/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1562, in _call_impl return forward_call(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/tiger/.pyenv/versions/3.11.2/lib/python3.11/site-packages/vllm/model_executor/models/deepseek_v2.py", line 504, in forward hidden_states = self.model(input_ids, positions, kv_caches, ^^^^^^^^^^^^^...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Process-1: Traceback (most recent call last): File "/home/tiger/.pyenv/versions/3.11.2/lib/python3.11/site-packages/vllm/worker/model_runner.py", line 1679, in capture output_hidden_or_intermediate_states = self.model(...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: L40 GPU deepseek-v2 fp8 cuda graph error; Using `--enforce-eager` can run properly. bug ### Your current environment ### Model Input Dumps python3 -m vllm.entrypoints.openai.api_server --model neuralmagic/DeepSee...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: File "/home/tiger/.pyenv/versions/3.11.2/lib/python3.11/site-packages/triton/runtime/jit.py", line 345, in return lambda *args, **kwargs: self.run(grid=grid, warmup=False, *args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: L40 GPU deepseek-v2 fp8 cuda graph error; Using `--enforce-eager` can run properly. bug ### Your current environment ### Model Input Dumps python3 -m vllm.entrypoints.openai.api_server --model neuralmagic/DeepSee...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 45, in return lambda *args, **kwargs: self.run(grid=grid, warmup=False, *args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/tiger/.pyenv/versions/3.11.2/lib/python3.11/site-packages/triton/ru...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
