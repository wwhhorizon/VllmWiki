# vllm-project/vllm#9402: [Bug]: Unable to infer QLoRA adapter using vLLM Docker

| 字段 | 值 |
| --- | --- |
| Issue | [#9402](https://github.com/vllm-project/vllm/issues/9402) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Unable to infer QLoRA adapter using vLLM Docker

### Issue 正文摘录

### Your current environment Docker version: 0.6.3 Base model id: TheBloke/WizardLM-13B-V1.2-GPTQ revision: gptq-8bit-128g-actorder_False LoRA Adapter: It is a custom adapter based on QLORA OS Version: Ubuntu 22.04 ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` docker run --name ocr_llm --gpus all --shm-size 1g -p 8010:8000 -v $volume:/data vllm/vllm-openai:latest --model $model --enable-lora --lora-modules $LORA_ADAPTERS --quantization gptq --gpu-memory-utilization 0.95 ``` ``` curl http://localhost:8010/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "adapter_id", "prompt": "San Francisco is a", "max_tokens": 7, "temperature": 0 }' | jq ``` When I tried to run the curl command, vllm docker crashed while giving the following error: ``` 2024-10-16T03:44:47.177951962Z INFO: 172.17.0.1:50230 - "POST /v1/completions HTTP/1.1" 500 Internal Server Error 2024-10-16T03:44:47.183535781Z INFO: Shutting down 2024-10-16T03:44:47.190118292Z ERROR 10-15 20:44:47 engine.py:160] RuntimeError('Error in model execution: Loading lora /data/adapters/container/checkpoint-2000 failed') 2024-10-16T03:44:47.190147783Z ERROR 10-15 20:44:47 engine.py:160] Traceback (m...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Unable to infer QLoRA adapter using vLLM Docker bug ### Your current environment Docker version: 0.6.3 Base model id: TheBloke/WizardLM-13B-V1.2-GPTQ revision: gptq-8bit-128g-actorder_False LoRA Adapter: It is a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: id: TheBloke/WizardLM-13B-V1.2-GPTQ revision: gptq-8bit-128g-actorder_False LoRA Adapter: It is a custom adapter based on QLORA OS Version: Ubuntu 22.04 ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` doc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 10-15 20:44:47 engine.py:160] self.set_active_loras(model_input.lora_requests, 2024-10-16T03:44:47.190254034Z ERROR 10-15 20:44:47 engine.py:160] File "/usr/local/lib/python3.12/dist-packages/vllm/worker/model_runner.py...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: enai:latest --model $model --enable-lora --lora-modules $LORA_ADAPTERS --quantization gptq --gpu-memory-utilization 0.95 ``` ``` curl http://localhost:8010/v1/completions \ -H "Content-Type: application/json" \ -d '{ "m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
