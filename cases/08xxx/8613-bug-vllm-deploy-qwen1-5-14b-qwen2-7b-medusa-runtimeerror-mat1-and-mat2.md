# vllm-project/vllm#8613: [Bug]: vllm deploy qwen1.5-14b/qwen2-7b+medusa, RuntimeError: mat1 and mat2 shapes cannot be multiplied (1x5120 and 4096x4096)

| 字段 | 值 |
| --- | --- |
| Issue | [#8613](https://github.com/vllm-project/vllm/issues/8613) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm deploy qwen1.5-14b/qwen2-7b+medusa, RuntimeError: mat1 and mat2 shapes cannot be multiplied (1x5120 and 4096x4096)

### Issue 正文摘录

### Your current environment vllm=0.6.1 ### Model Input Dumps CUDA_VISIBLE_DEVICES=7 python3 -m vllm.entrypoints.openai.api_server --port 8010 \ --served-model-name qwen2-7b \ --model /mnt/user/deploy/qwen15_14b_finetuning_chatbot_v1_0914_deploy --dtype auto -tp 1 \ --max-model-len 4096 --gpu-memory-utilization 0.9 \ --max-num-seqs 1 \ --speculative-model /mnt/user/deploy/qwen15_14b_finetuning_chatbot_v1_0914_deploy/medusa \ --speculative-draft-tensor-parallel-size 1 \ --num-speculative-tokens 3 \ --speculative-disable-by-batch-size 3 \ --use-v2-block-manager \ --spec-decoding-acceptance-method typical_acceptance_sampler ### 🐛 Describe the bug ERROR 09-19 10:53:38 async_llm_engine.py:63] Engine background task failed ERROR 09-19 10:53:38 async_llm_engine.py:63] Traceback (most recent call last): ERROR 09-19 10:53:38 async_llm_engine.py:63] File "/opt/conda/envs/vllm/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 53, in _log_task_completion ERROR 09-19 10:53:38 async_llm_engine.py:63] return_value = task.result() ERROR 09-19 10:53:38 async_llm_engine.py:63] File "/opt/conda/envs/vllm/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 939, in ru...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: x-model-len 4096 --gpu-memory-utilization 0.9 \ --max-num-seqs 1 \ --speculative-model /mnt/user/deploy/qwen15_14b_finetuning_chatbot_v1_0914_deploy/medusa \ --speculative-draft-tensor-parallel-size 1 \ --num-speculativ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm deploy qwen1.5-14b/qwen2-7b+medusa, RuntimeError: mat1 and mat2 shapes cannot be multiplied (1x5120 and 4096x4096) bug ### Your current environment vllm=0.6.1 ### Model Input Dumps CUDA_VISIBLE_DEVICES=7 pyt...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: --model /mnt/user/deploy/qwen15_14b_finetuning_chatbot_v1_0914_deploy --dtype auto -tp 1 \ --max-model-len 4096 --gpu-memory-utilization 0.9 \ --max-num-seqs 1 \ --speculative-model /mnt/user/deploy/qwen15_14b_finetunin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 096) bug ### Your current environment vllm=0.6.1 ### Model Input Dumps CUDA_VISIBLE_DEVICES=7 python3 -m vllm.entrypoints.openai.api_server --port 8010 \ --served-model-name qwen2-7b \ --model /mnt/user/deploy/qwen15_14...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: culative-tokens 3 \ --speculative-disable-by-batch-size 3 \ --use-v2-block-manager \ --spec-decoding-acceptance-method typical_acceptance_sampler ### 🐛 Describe the bug ERROR 09-19 10:53:38 async_llm_engine.py:63] Engin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
