# vllm-project/vllm#26137: [Bug]: Assertion in AgRsAll2AllManager in DP+EP

| 字段 | 值 |
| --- | --- |
| Issue | [#26137](https://github.com/vllm-project/vllm/issues/26137) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Assertion in AgRsAll2AllManager in DP+EP

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running DataParallel + ExpertParallel for MoE models we get an assertion in AgRsAll2AllManager: ``` File "/home/imarkov/repos/vllm/vllm/distributed/device_communicators/all2all.py", line 120, in dispatch assert sizes[dist_group.rank_in_group] == hidden_states.shape[0] ``` Reproduce script: ``` Server: vllm serve deepseek-ai/DeepSeek-V2-Lite-Chat --disable-log-requests --no-enable-prefix-caching -tp 1 -dp 2 --max-num-seqs 256 --enable-expert-parallel --load-format dummy --gpu-memory-utilization 0.85 Client: vllm bench serve --port 8000 --model deepseek-ai/DeepSeek-V2-Lite-Chat --dataset-name random --num-prompts 4 --random-input-len 1024 --random-output-len 1 --trust-remote-code ``` With `--enforce-eager` setting it doesn't fail. For `--random-input-len` <= 512 it doesn't fail. But it fails with `-O.cudagraph_mode=NONE -O.use_inductor=False` Prints of the sizes before the `assert`: ``` rank: 1, dp rank: 1, sizes: 1024, hidden_states.shape: torch.Size([1, 2048]) # causes the assertion rank: 0, dp rank: 0, sizes: 1024, hidden_states.shape: torch.Size([1024, 2048]) ``` ### Before submitting a new issue... - [x] Make sure you already...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### 🐛 Describe the bug Running DataParallel + ExpertParallel for MoE models we get an assertion in AgRsAll2AllManager: ``` File "/home/imarkov/repos/vllm/vllm/distributed/device_communicators/all2all.py", line 120, in d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding cud...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: pos/vllm/vllm/distributed/device_communicators/all2all.py", line 120, in dispatch assert sizes[dist_group.rank_in_group] == hidden_states.shape[0] ``` Reproduce script: ``` Server: vllm serve deepseek-ai/DeepSeek-V2-Lit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: For `--random-input-len` <= 512 it doesn't fail. But it fails with `-O.cudagraph_mode=NONE -O.use_inductor=False` Prints of the sizes before the `assert`: ``` rank: 1, dp rank: 1, sizes: 1024, hidden_states.shape: torch...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: r current environment ### 🐛 Describe the bug Running DataParallel + ExpertParallel for MoE models we get an assertion in AgRsAll2AllManager: ``` File "/home/imarkov/repos/vllm/vllm/distributed/device_communicators/all2a...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
