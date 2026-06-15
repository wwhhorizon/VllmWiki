# vllm-project/vllm#9253: [Bug]: new beam search implementation ignores stop conditions

| 字段 | 值 |
| --- | --- |
| Issue | [#9253](https://github.com/vllm-project/vllm/issues/9253) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: new beam search implementation ignores stop conditions

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Command used to serve `vllm serve $MODEL --port $PORT --gpu-memory-utilization 0.97 --max-model-len 4096 --dtype "auto" --trust-remote-code --enable-prefix-caching --disable-log-requests --num_scheduler-steps 1 --max-num-seqs 128` Tried with `MODEL="hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4"` and `"hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4"`, vllm served via OpenAI, nightly build + `python_only_dev.py` Both models ignore stop conditions specified in `client.completions.create` when run with beam search. It appears to me that they actually generate up to the requested number of `max_tokens` regardless whether tokens in stop or ` ` were produced. For an example, run the code below. NB: I am using `n=4` for beam search since the API commits seem to suggest that this is how you pass the number of beams now. ```python # ... assume you have a client and a model_id tokenizer = AutoTokenizer.from_pretrained(model_id) # Create a simple conversation prompt system_prompt = "You are a helpful assistant that continues number sequences." user_prompt = "Please continue this sequence: one, t...

## 现有链接修复摘要

#9264 [Frontend, Core] Adding stop and stop_token_ids for beam search.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: new beam search implementation ignores stop conditions bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Command used to serve `vllm serve $MODEL --port $PORT --gpu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: s/Meta-Llama-3.1-8B-Instruct-AWQ-INT4"`, vllm served via OpenAI, nightly build + `python_only_dev.py` Both models ignore stop conditions specified in `client.completions.create` when run with beam search. It appears to...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: $MODEL --port $PORT --gpu-memory-utilization 0.97 --max-model-len 4096 --dtype "auto" --trust-remote-code --enable-prefix-caching --disable-log-requests --num_scheduler-steps 1 --max-num-seqs 128` Tried with `MODEL="hug...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: new beam search implementation ignores stop conditions bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Command used to serve `vllm serve $MODEL --port $PORT --gpu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: n ignores stop conditions bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Command used to serve `vllm serve $MODEL --port $PORT --gpu-memory-utilization 0.97 --max-model...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9264](https://github.com/vllm-project/vllm/pull/9264) | closes_keyword | 0.95 | [Frontend, Core] Adding stop and stop_token_ids for beam search. | fix to #9253 Update 15/10: PR updated post-merge of beam search methods. - Removing the `eos` check led to no stopping in chat modes, I keep it as it is. - Is fairly simpli |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
