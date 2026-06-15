# vllm-project/vllm#20514: [Bug]:  _Z35cutlass_blockwise_scaled_grouped_mmRN2at6TensorERKS0_S3_S3_S3_S3_S3_

| 字段 | 值 |
| --- | --- |
| Issue | [#20514](https://github.com/vllm-project/vllm/issues/20514) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  _Z35cutlass_blockwise_scaled_grouped_mmRN2at6TensorERKS0_S3_S3_S3_S3_S3_

### Issue 正文摘录

### Your current environment ```text 2 x RTX 6000 PRO python -m vllm.entrypoints.api_server --model cognitivecomputations/Qwen3-235B-A22B-AWQ --enable-reasoning --reasoning-parser deepseek_r1 -tp 2 ImportError: /home/giga/vllm/vllm/_C.abi3.so: undefined symbol: _Z35cutlass_blockwise_scaled_grouped_mmRN2at6TensorERKS0_S3_S3_S3_S3_S3_ ``` ### How you are installing vllm ```sh Verified NVIDIA-SMI for Driver 575.62 and CUDA 12.9 git clone https://github.com/vllm-project/vllm.git cd vllm python -m venv vllm source ./vllm/bin/activate pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu129 # note changed cu128 to cu129 python use_existing_torch.py python -m pip install -r requirements/build.txt python -m pip install -r requirements/common.txt python -m pip install -e . --no-build-isolation -v ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: _Z35cutlass_blockwise_scaled_grouped_mmRN2at6TensorERKS0_S3_S3_S3_S3_S3_ installation ### Your current environment ```text 2 x RTX 6000 PRO python -m vllm.entrypoints.api_server --model cognitivecomputations/Qwen3-235B-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: 0_S3_S3_S3_S3_S3_ installation ### Your current environment ```text 2 x RTX 6000 PRO python -m vllm.entrypoints.api_server --model cognitivecomputations/Qwen3-235B-A22B-AWQ --enable-reasoning --reasoning-parser deepseek...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: _Z35cutlass_blockwise_scaled_grouped_mmRN2at6TensorERKS0_S3_S3_S3_S3_S3_ installation ### Your current environment ```text 2 x RTX 6000 PRO python -m vllm.entrypoints.api_server --model cognitivecomputations/Qwen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nment ```text 2 x RTX 6000 PRO python -m vllm.entrypoints.api_server --model cognitivecomputations/Qwen3-235B-A22B-AWQ --enable-reasoning --reasoning-parser deepseek_r1 -tp 2 ImportError: /home/giga/vllm/vllm/_C.abi3.so...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: _Z35cutlass_blockwise_scaled_grouped_mmRN2at6TensorERKS0_S3_S3_S3_S3_S3_ installation ### Your current environment ```text 2 x RTX 6000 PRO python -m vllm.entrypoints.api_server --model cognitivecomputations/Qwen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
