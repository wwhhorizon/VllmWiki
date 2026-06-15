# vllm-project/vllm#761: WizardCoder 15B not given proper output

| 字段 | 值 |
| --- | --- |
| Issue | [#761](https://github.com/vllm-project/vllm/issues/761) |
| 状态 | closed |
| 标签 |  |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> WizardCoder 15B not given proper output

### Issue 正文摘录

I have started the vllm server using the below command: `CUDA_VISIBLE_DEVICES=0,1 python -m vllm.entrypoints.api_server --model WizardLM/WizardCoder-15B-V1.0 --tensor-parallel-size 2 --trust-remote-code ` Output of which is : ```2023-08-14 20:16:51,729 INFO worker.py:1621 -- Started a local Ray instance. INFO 08-14 20:16:52 llm_engine.py:70] Initializing an LLM engine with config: model='WizardLM/WizardCoder-15B-V1.0', tokenizer='WizardLM/WizardCoder-15B-V1.0', tokenizer_mode=auto, trust_remote_code=True, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=2, seed=0) INFO 08-14 20:17:33 llm_engine.py:196] # GPU blocks: 803, # CPU blocks: 546 INFO: Started server process [41444] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://localhost:8080 (Press CTRL+C to quit) ``` Then I try to query this endpoint using below command: ```python -m api_client --port 8080 --host localhost --prompt "What does .forEach() do?" --stream``` Output of which is: ```Prompt: 'What does .forEach() do?' Beam candidate 0: 'What does .forEach() do?' Beam candidate 1: 'What does .forEach() do?\n.__...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: rdLM/WizardCoder-15B-V1.0', tokenizer_mode=auto, trust_remote_code=True, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=2, seed=0) INFO 08-14 20:17:33 llm_eng...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: e=auto, trust_remote_code=True, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=2, seed=0) INFO 08-14 20:17:33 llm_engine.py:196] # GPU blocks: 803, # CPU bloc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: mmand: `CUDA_VISIBLE_DEVICES=0,1 python -m vllm.entrypoints.api_server --model WizardLM/WizardCoder-15B-V1.0 --tensor-parallel-size 2 --trust-remote-code ` Output of which is : ```2023-08-14 20:16:51,729 INFO worker.py:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 03, # CPU blocks: 546 INFO: Started server process [41444] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://localhost:8080 (Press CTRL+C to quit) ``` Then I try...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n proper output I have started the vllm server using the below command: `CUDA_VISIBLE_DEVICES=0,1 python -m vllm.entrypoints.api_server --model WizardLM/WizardCoder-15B-V1.0 --tensor-parallel-size 2 --trust-remote-code...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
