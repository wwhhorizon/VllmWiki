# vllm-project/vllm#34661: [Bug]: SyntaxError in qwen3_5_moe.py line 81 when loading Qwen3.5-397B-A17B

| 字段 | 值 |
| --- | --- |
| Issue | [#34661](https://github.com/vllm-project/vllm/issues/34661) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;quantization;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | fp8;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: SyntaxError in qwen3_5_moe.py line 81 when loading Qwen3.5-397B-A17B

### Issue 正文摘录

## Describe the bug vLLM crashes with a Python SyntaxError when attempting to load the Qwen3.5-397B-A17B model. The error occurs in `/usr/local/lib/python3.12/dist-packages/vllm/transformers_utils/configs/qwen3_5_moe.py` at line 81, indicating a mismatched parenthesis/bracket on line 78. ``` SyntaxError: closing parenthesis ']' does not match opening parenthesis '{' on line 78 ``` This is a syntax error in vLLM's source code itself, making the file syntactically invalid Python. ## Environment - **vLLM Version**: 0.16.0rc2.dev216+g5bff999d1 (nightly build) - **Docker Image**: `vllm/vllm-openai:nightly` - **Python Version**: 3.12 - **Model**: Qwen/Qwen3.5-397B-A17B (FP8 quantized) - **GPUs**: 4x NVIDIA H200 NVL 141GB - **Deployment**: Docker on OpenShift/Kubernetes ## Reproduction Steps ```bash vllm serve Qwen/Qwen3.5-397B-A17B \ --tensor-parallel-size 4 \ --max-model-len 32768 \ --gpu-memory-utilization 0.9 \ --quantization fp8 \ --trust-remote-code \ --reasoning-parser qwen3 ``` 3. vLLM crashes during model config loading with SyntaxError ## Full Error Traceback ``` (APIServer pid=48) Traceback (most recent call last): (APIServer pid=48) File "/usr/local/bin/vllm", line 10, in (AP...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: making the file syntactically invalid Python. ## Environment - **vLLM Version**: 0.16.0rc2.dev216+g5bff999d1 (nightly build) - **Docker Image**: `vllm/vllm-openai:nightly` - **Python Version**: 3.12 - **Model**: Qwen/Qw...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: SyntaxError in qwen3_5_moe.py line 81 when loading Qwen3.5-397B-A17B ## Describe the bug vLLM crashes with a Python SyntaxError when attempting to load the Qwen3.5-397B-A17B model. The error occurs in `/usr/local...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ightly` - **Python Version**: 3.12 - **Model**: Qwen/Qwen3.5-397B-A17B (FP8 quantized) - **GPUs**: 4x NVIDIA H200 NVL 141GB - **Deployment**: Docker on OpenShift/Kubernetes ## Reproduction Steps ```bash vllm serve Qwen/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: m/entrypoints/cli/main.py", line 73, in main (APIServer pid=48) args.dispatch_function(args) (APIServer pid=48) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 112, in cmd (APIServer p...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: vllm/transformers_utils/configs/qwen3_5_moe.py` at line 81, indicating a mismatched parenthesis/bracket on line 78. ``` SyntaxError: closing parenthesis ']' does not match opening parenthesis '{' on line 78 ``` This is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
