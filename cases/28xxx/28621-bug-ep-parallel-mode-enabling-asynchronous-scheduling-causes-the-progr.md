# vllm-project/vllm#28621: [Bug]: EP parallel mode, enabling asynchronous scheduling causes the program to  crash

| 字段 | 值 |
| --- | --- |
| Issue | [#28621](https://github.com/vllm-project/vllm/issues/28621) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;moe;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EP parallel mode, enabling asynchronous scheduling causes the program to  crash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I found that in the EP parallel mode, enabling asynchronous scheduling causes the program to crash ``` vllm bench serve --host ${CHIEF_IP} --port 8021 --ignore-eos --random-input-len 9429 --random-output-len 1524 --num-prompts 1000 --max-concurrency 84 --model hunyuan_a30b_fp8_static ``` server launch cmd: ``` export NCCL_ALGO=Ring export NCCL_PRIMS_PROFILE_ENABLE=0 export MODEL_PATH=/home/hunyuan_a30b_fp8_static/ export MAX_MODEL_SEQ_LEN=94208 export MAX_BATCH_SIZE=128 export TIMESTAMP=`date +%Y%m%d_%H%M` vllm serve ${MODEL_PATH} \ -tp 8 \ --enable-expert-parallel \ --enable-eplb \ --trust_remote_code \ --block-size 64 \ --load-format "runai_streamer" \ --model-loader-extra-config '{"concurrency":16}' \ --max_model_len ${MAX_MODEL_SEQ_LEN} \ --port 8021 \ --no-enable-prefix-caching --no-enable-chunked-prefill \ --max-num-seqs ${MAX_BATCH_SIZE} \ --served-model-name ${SERVED_MODEL_NAME} \ --max-num-batched-tokens 45056 \ --max-prompt-len 28672 \ --gpu-memory-utilization 0.8 \ --async-scheduling \ --disable-log-requests \ ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked t...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: rt 8021 \ --no-enable-prefix-caching --no-enable-chunked-prefill \ --max-num-seqs ${MAX_BATCH_SIZE} \ --served-model-name ${SERVED_MODEL_NAME} \ --max-num-batched-tokens 45056 \ --max-prompt-len 28672 \ --gpu-memory-uti...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;scheduler_memory;speculative_decoding cuda;moe;operator;triton build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 429 --random-output-len 1524 --num-prompts 1000 --max-concurrency 84 --model hunyuan_a30b_fp8_static ``` server launch cmd: ``` export NCCL_ALGO=Ring export NCCL_PRIMS_PROFILE_ENABLE=0 export MODEL_PATH=/home/hunyuan_a3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: rallel \ --enable-eplb \ --trust_remote_code \ --block-size 64 \ --load-format "runai_streamer" \ --model-loader-extra-config '{"concurrency":16}' \ --max_model_len ${MAX_MODEL_SEQ_LEN} \ --port 8021 \ --no-enable-prefi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
