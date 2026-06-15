# vllm-project/vllm#12008: [Bug]: Nccl Test Error

| 字段 | 值 |
| --- | --- |
| Issue | [#12008](https://github.com/vllm-project/vllm/issues/12008) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Nccl Test Error

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vLLM NCCL test failed test image is: /vllm/vllm-openai:latest vllm version is: 0.6.6.post1 docker commad is: ``` docker run -id --name test --network host --ipc=host -e NVIDIA_VISIBLE_DEVICES=2,3 -v `pwd`:/models --entrypoint=bash vllm/vllm-openai:latest ``` test.py: https://docs.vllm.ai/en/latest/getting_started/troubleshooting.html#incorrect-hardware-driver NCCL_DEBUG=TRACE torchrun --nproc-per-node=2 test.py ``` PyTorch NCCL is successful! PyTorch GLOO is successful! PyTorch GLOO is successful! INFO 01-13 04:05:17 utils.py:918] Found nccl from library libnccl.so.2 INFO 01-13 04:05:17 utils.py:918] Found nccl from library libnccl.so.2 INFO 01-13 04:05:17 pynccl.py:69] vLLM is using nccl==2.21.5 INFO 01-13 04:05:17 pynccl.py:69] vLLM is using nccl==2.21.5 bm-22075ry:1259:1259 [0] NCCL INFO Using non-device net plugin version 0 bm-22075ry:1260:1260 [1] NCCL INFO Using non-device net plugin version 0 bm-22075ry:1259:1259 [0] NCCL INFO Using network Socket bm-22075ry:1260:1260 [1] NCCL INFO Using network Socket bm-22075ry:1259:1259 [0] NCCL INFO ncclCommInitRank comm 0xc4cbfc0 rank 0 nranks 2 cud...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: bug vLLM NCCL test failed test image is: /vllm/vllm-openai:latest vllm version is: 0.6.6.post1 docker commad is: ``` docker run -id --name test --network host --ipc=host -e NVIDIA_VISIBLE_DEVICES=2,3 -v `pwd`:/models --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: :1259:1259 [0] NCCL INFO ncclCommInitRank comm 0xc4cbfc0 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 48000 commId 0x9ff7e868477ca4f8 - Init START bm-22075ry:1260:1260 [1] NCCL INFO ncclCommInitRank comm 0xbea9880 rank 1 n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Nccl Test Error bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vLLM NCCL test failed test image is: /vllm/vllm-openai:latest vllm version is: 0.6.6.post1 docker...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: this process. In rare cases this process can exit before this point and block the progress of another member of the process group. This constraint has always been present, but this warning has only been added since PyTo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Nccl Test Error bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vLLM NCCL test failed test image is: /vllm/vllm-openai:latest vllm version is: 0.6.6.post1 docker...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
