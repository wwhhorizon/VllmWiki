# vllm-project/vllm#26582: [Bug]: which triton-kernels version for MXFP4 Triton backend?

| 字段 | 值 |
| --- | --- |
| Issue | [#26582](https://github.com/vllm-project/vllm/issues/26582) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: which triton-kernels version for MXFP4 Triton backend?

### Issue 正文摘录

### Your current environment vllm v0.11.0 installed via `uv pip install vllm --torch-backend=auto` triton + triton-kernels at different commits installed from source ### 🐛 Describe the bug **Which triton + triton-kernels version does one have to install to run GPT-OSS with the MXFP4 Triton backend?** No matter which version I try, I always get an error `Failed to import Triton kernels. Please make sure your triton version is compatible.` Clearly, the latest triton-kernels will not work since the code in `vllm.model_executor.layers.fused_moe.gpt_oss_triton_kernels_moe` tries to import from `triton_kernels.routing`, but `triton_kernels.routing` has been deprecated (cf. https://github.com/triton-lang/triton/commit/30ede52aa2aecfd2ab3d6672ed21bbf4eb6438b3). But also with older versions I get errors like `ImportError: cannot import name 'triton_key' from 'triton.compiler.compiler` or `Error: No module named 'triton.language.target_info`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently ask...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: which triton-kernels version for MXFP4 Triton backend? bug ### Your current environment vllm v0.11.0 installed via `uv pip install vllm --torch-backend=auto` triton + triton-kernels at different commits installed...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: which triton-kernels version for MXFP4 Triton backend? bug ### Your current environment vllm v0.11.0 installed via `uv pip install vllm --torch-backend=auto` triton + triton-kernels at different commits installed...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: which triton-kernels version for MXFP4 Triton backend? bug ### Your current environment vllm v0.11.0 installed via `uv pip install vllm --torch-backend=auto` triton + triton-kernels at different commits installed...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: **Which triton + triton-kernels version does one have to install to run GPT-OSS with the MXFP4 Triton backend?** No matter which version I try, I always get an error `Failed to import Triton kernels. Please make sure yo...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ernels will not work since the code in `vllm.model_executor.layers.fused_moe.gpt_oss_triton_kernels_moe` tries to import from `triton_kernels.routing`, but `triton_kernels.routing` has been deprecated (cf. https://githu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
