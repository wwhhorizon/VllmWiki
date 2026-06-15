# vllm-project/vllm#18761: [Bug]: [0.9.0] llama-3-8b-instruct-awq returns `name 'FusedMoEPermuteExpertsUnpermute' is not defined` error

| 字段 | 值 |
| --- | --- |
| Issue | [#18761](https://github.com/vllm-project/vllm/issues/18761) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [0.9.0] llama-3-8b-instruct-awq returns `name 'FusedMoEPermuteExpertsUnpermute' is not defined` error

### Issue 正文摘录

### Your current environment Using ubuntu:22.04 docker image and running inside docker: ```bash ENV PIP_EXTRA_INDEX_URL="https://download.pytorch.org/whl/cpu" ENV VLLM_TARGET_DEVICE="cpu" RUN pip install -v git+https://github.com/vllm-project/vllm@v0.9.0 RUN pip install intel_extension_for_pytorch==2.7.0 ``` ### 🐛 Describe the bug Running model `casperhansen/llama-3-8b-instruct-awq` with params: `--model casperhansen/llama-3-8b-instruct-awq --device cpu --tensor-parallel-size 1 --pipeline-parallel-size 1 --dtype bfloat16 --max-num-seqs 256 --max-model-len 4096 --download_dir /data --host 0.0.0.0 --port 80` on version 0.9.0 returns following error: ```python llm-vllm-model-server | [W527 10:31:54.634480995 OperatorEntry.cpp:154] Warning: Warning only once for all operators, other operators may also be overridden. llm-vllm-model-server | Overriding a previously registered kernel for the same operator and the same dispatch key llm-vllm-model-server | operator: aten::_addmm_activation(Tensor self, Tensor mat1, Tensor mat2, *, Scalar beta=1, Scalar alpha=1, bool use_gelu=False) -> Tensor llm-vllm-model-server | registered at /pytorch/build/aten/src/ATen/RegisterSchema.cpp:6 llm-vllm-mo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: not defined` error bug ### Your current environment Using ubuntu:22.04 docker image and running inside docker: ```bash ENV PIP_EXTRA_INDEX_URL="https://download.pytorch.org/whl/cpu" ENV VLLM_TARGET_DEVICE="cpu" RUN pip...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: t-awq --device cpu --tensor-parallel-size 1 --pipeline-parallel-size 1 --dtype bfloat16 --max-num-seqs 256 --max-model-len 4096 --download_dir /data --host 0.0.0.0 --port 80` on version 0.9.0 returns following error: ``...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: [0.9.0] llama-3-8b-instruct-awq returns `name 'FusedMoEPermuteExpertsUnpermute' is not defined` error bug ### Your current environment Using ubuntu:22.04 docker image and running inside docker: ```bash ENV PIP_EX...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: [0.9.0] llama-3-8b-instruct-awq returns `name 'FusedMoEPermuteExpertsUnpermute' is not defined` error bug ### Your current environment Using ubuntu:22.04 docker image and running inside docker: ```bash ENV PIP_EX...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: riding a previously registered kernel for the same operator and the same dispatch key llm-vllm-model-server | operator: aten::_addmm_activation(Tensor self, Tensor mat1, Tensor mat2, *, Scalar beta=1, Scalar alpha=1, bo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
