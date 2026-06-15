# vllm-project/vllm#14120: [Bug]: last gpu always OOM when only use pipeline parallelism with 2 nodes x 8cards

| 字段 | 值 |
| --- | --- |
| Issue | [#14120](https://github.com/vllm-project/vllm/issues/14120) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: last gpu always OOM when only use pipeline parallelism with 2 nodes x 8cards

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 【PROBLEM】 I have a Deepseek R1 HuggingFace gptq model(our own model) with a size of 647G. I use vllm to load it with two nodes, and each node has 8cards * 80g. I set --pipeline-parallel-size 16. The entire command is as follows. Then the last gpu(15th of 16) OOM when loading. I set VLLM_PP_LAYER_PARTITION='4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1', but still failed with OOM. The last gpu always OOM: ![Image](https://github.com/user-attachments/assets/7aa63a32-0fe5-4ca6-afef-c4c63181ef59) 【COMMAND:】 ==start ray== bash run_cluster.sh vllm/vllm-openai x.y.z.210 --head /data/LM/hf/DeepSeek-R1-Int8/ -e VLLM_HOST_IP=x.y.z.210 bash run_cluster.sh vllm/vllm-openai x.y.z.210 --worker /data/LM/hf/DeepSeek-R1-Int8/ -e VLLM_HOST_IP=x.y.z.209 ==start serve== vllm serve /root/.cache/huggingface/ --enable-reasoning --reasoning-parser deepseek_r1 --pipeline-parallel-size 16 --trust-remote-code --gpu-memory-utilization 0.9 --dtype bfloat16 【error stack】 root@lyg0210:~/.cache/huggingface# vllm serve /root/.cache/huggingface/ --enable-reasoning --reasoning-parser deepseek_r1 --pipeline-parallel-size 16 --trust-remote-code --gpu-memory-utilization 0.9 --dtyp...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: always OOM when only use pipeline parallelism with 2 nodes x 8cards bug;stale ### Your current environment ### 🐛 Describe the bug 【PROBLEM】 I have a Deepseek R1 HuggingFace gptq model(our own model) with a size of 647G....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ed platform cuda. INFO 03-02 00:35:21 api_server.py:912] vLLM API server version 0.7.3 INFO 03-02 00:35:21 api_server.py:913] args: Namespace(subparser='serve', model_tag='/root/.cache/huggingface/', config='', host=Non...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: line-parallel-size 16 --trust-remote-code --gpu-memory-utilization 0.9 --dtype bfloat16 【error stack】 root@lyg0210:~/.cache/huggingface# vllm serve /root/.cache/huggingface/ --enable-reasoning --reasoning-parser deepsee...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: ='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_o rigins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=No...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: t environment ### 🐛 Describe the bug 【PROBLEM】 I have a Deepseek R1 HuggingFace gptq model(our own model) with a size of 647G. I use vllm to load it with two nodes, and each node has 8cards * 80g. I set --pipeline-paral...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
