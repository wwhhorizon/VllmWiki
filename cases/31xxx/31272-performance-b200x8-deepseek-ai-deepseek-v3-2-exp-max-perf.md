# vllm-project/vllm#31272: [Performance]: b200x8 deepseek-ai/DeepSeek-V3.2-Exp max perf

| 字段 | 值 |
| --- | --- |
| Issue | [#31272](https://github.com/vllm-project/vllm/issues/31272) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: b200x8 deepseek-ai/DeepSeek-V3.2-Exp max perf

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression Do you have any ideas on how to increase TPS? I have two servers — one with H200 ×8 and another with B200 ×8. They use the same startup script, but the performance is almost identical. In my opinion, B200 should be faster than H200, so maybe my settings are not optimal vllm serve \ --model deepseek-ai/DeepSeek-V3.2-Exp \ --served-model-name deepseek-ai/DeepSeek-V3.2-Exp \ --host 0.0.0.0 \ --port 12345 \ --tensor-parallel-size 8 \ --enable-auto-tool-choice \ --tool-call-parser deepseek_v31 \ --chat-template /root/tool_chat_template_deepseekv31.jinja \ --gpu-memory-utilization 0.9 \ --max-model-len 125000 \ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Performance]: b200x8 deepseek-ai/DeepSeek-V3.2-Exp max perf performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Do you have any ideas on how to increase TPS? I have...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: aster than H200, so maybe my settings are not optimal vllm serve \ --model deepseek-ai/DeepSeek-V3.2-Exp \ --served-model-name deepseek-ai/DeepSeek-V3.2-Exp \ --host 0.0.0.0 \ --port 12345 \ --tensor-parallel-size 8 \ -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.3 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves avx_vnni avx512_bf16 clzero xsaveerptr wbnoinvd arat npt lbrv nrip_save tsc_scale vmcb_clean flushbyasid pausefilter pfthreshold v_vmsave_vmload vgif vnmi avx512vb...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
