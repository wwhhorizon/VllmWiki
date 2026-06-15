# vllm-project/vllm#38307: [Bug]: AMD's minimax mxfp4 trust_remote_code bug

| 字段 | 值 |
| --- | --- |
| Issue | [#38307](https://github.com/vllm-project/vllm/issues/38307) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AMD's minimax mxfp4 trust_remote_code bug

### Issue 正文摘录

### Your current environment image: `vllm/vllm-openai-rocm:v0.17.1` ### 🐛 Describe the bug already filed via slack last friday but want to file here to track it. blocker for merging this PR in https://github.com/SemiAnalysisAI/InferenceX/pull/827 even when doing trust_remote_code=true, minimax mxfp4 doesnt use it leading to this bug. seems like @hongxiayang already working on fixing it https://github.com/vllm-project/vllm/pull/37698 https://github.com/SemiAnalysisAI/InferenceX/actions/runs/23326389246/job/67848378566?pr=827 ``` + vllm serve amd/MiniMax-M2.5-MXFP4 --port 8888 --tensor-parallel-size=2 --gpu-memory-utilization 0.95 --max-model-len 2248 --block-size=32 --trust-remote-code WARNING 03-20 02:24:48 [gpt_oss_triton_kernels_moe.py:56] Using legacy triton_kernels on ROCm /usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/chat_completion/protocol.py:346: SyntaxWarning: invalid escape sequence '\e' "(e.g. 'abcdabcdabcd...' or '\emoji \emoji \emoji ...'). This feature " /usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/completion/protocol.py:176: SyntaxWarning: invalid escape sequence '\e' "(e.g. 'abcdabcdabcd...' or '\emoji \emoji \emoji ...'). This...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: =1169773) INFO 03-20 02:24:49 [utils.py:302] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.17.1 (APIServer pid=1169773) INFO 03-20 02:24:49 [utils.py:302] █▄█▀ █ █ █ █ model amd/MiniMax-M2.5-MXFP4 (APIServer pid=1169773) INFO 03-20 02:24...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: --port 8888 --tensor-parallel-size=2 --gpu-memory-utilization 0.95 --max-model-len 2248 --block-size=32 --trust-remote-code WARNING 03-20 02:24:48 [gpt_oss_triton_kernels_moe.py:56] Using legacy triton_kernels on ROCm /...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 2248 --block-size=32 --trust-remote-code WARNING 03-20 02:24:48 [gpt_oss_triton_kernels_moe.py:56] Using legacy triton_kernels on ROCm /usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/chat_completion/prot...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: AMD's minimax mxfp4 trust_remote_code bug bug;rocm ### Your current environment image: `vllm/vllm-openai-rocm:v0.17.1` ### 🐛 Describe the bug already filed via slack last friday but want to file here to track it....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: AMD's minimax mxfp4 trust_remote_code bug bug;rocm ### Your current environment image: `vllm/vllm-openai-rocm:v0.17.1` ### 🐛 Describe the bug already filed via slack last friday but want to file here to track it....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
