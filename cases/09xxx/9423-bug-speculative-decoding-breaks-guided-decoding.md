# vllm-project/vllm#9423: [Bug]: Speculative decoding breaks guided decoding.

| 字段 | 值 |
| --- | --- |
| Issue | [#9423](https://github.com/vllm-project/vllm/issues/9423) |
| 状态 | closed |
| 标签 | bug;structured-output;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Speculative decoding breaks guided decoding.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I run the vLLM server with speculative decoding as follows: ```.py NCCL_GRAPH_FILE="/home/azureuser/apps/ai-kyc_vu/vllm_server/gpu_graph.xml" python -m vllm.entrypoints.openai.api_server --model "neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8" --served-model-name "" --guided-decoding-backend "outlines" --gpu-memory-utilization 0.9 --port 7999 --worker_use_ray --max-model-len 40000 --tensor-parallel-size 2 --speculative-model="[ngram]" --num_speculative_tokens 5 --ngram_prompt_lookup_max=4 --use-v2-block-manager ``` I then prompt the LLM with guided json created from the following pydantic model: ```.py class A(BaseModel): a: int ``` I incorporate the guided json into the following testing prompt: ```.json { "model": "", "messages": [ { "role": "system", "content": "" }, { "role": "user", "content": "How are you?" } ], "guided_decoding_backend": "outlines", "guided_json": {"properties": {"a": {"title": "A", "type": "integer"}}, "required": ["a"], "title": "A", "type": "object"}, "max_tokens": 200, "top_k": 1, "stream": false } ``` The json guidance should ensure that the output is a valid json obje...

## 现有链接修复摘要

#12537 [Bugfix][Spec Decode][V0] fix: update logits processor for MQA scoring

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Speculative decoding breaks guided decoding. bug;structured-output;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I run the vLLM server with speculative decoding as f
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cuda;...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: oints.openai.api_server --model "neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8" --served-model-name "" --guided-decoding-backend "outlines" --gpu-memory-utilization 0.9 --port 7999 --worker_use_ray --max-model-len 40000 -...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [ngram]" --num_speculative_tokens 5 --ngram_prompt_lookup_max=4 --use-v2-block-manager ``` I then prompt the LLM with guided json created from the following pydantic model: ```.py class A(BaseModel): a: int ``` I incorp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ce. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#12537](https://github.com/vllm-project/vllm/pull/12537) | closes_keyword | 0.95 | [Bugfix][Spec Decode][V0] fix: update logits processor for MQA scoring | FIX #9423 ## Summary - In issue #9423, the MQA scorer sampled different tokens than the BatchExpansion scorer, even when using the greedy option. - The model itself produced the |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
