# vllm-project/vllm#6023: [Bug]: After enabling APC, concurrent processing of requests will result in error and return responses from other requests.

| 字段 | 值 |
| --- | --- |
| Issue | [#6023](https://github.com/vllm-project/vllm/issues/6023) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: After enabling APC, concurrent processing of requests will result in error and return responses from other requests.

### Issue 正文摘录

### Your current environment ```text vllm version：0.5.0 model: qwen-14b ``` ### 🐛 Describe the bug ``` self.model = LLM(model=model_dir, tokenizer=model_dir, tensor_parallel_size=tensor_parallel_size, trust_remote_code=trust_remote_code, quantization=quantization, gpu_memory_utilization=gpu_memory_utilization, dtype=dtype, enable_prefix_caching=True) batch_out_ids = self.model.generate( batch_raw_text, generation_config=self.model.generation_config, prompt_token_ids=batch_context_tokens ) ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: r requests. bug ### Your current environment ```text vllm version：0.5.0 model: qwen-14b ``` ### 🐛 Describe the bug ``` self.model = LLM(model=model_dir, tokenizer=model_dir, tensor_parallel_size=tensor_parallel_size,
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: trust_remote_code=trust_remote_code, quantization=quantization, gpu_memory_utilization=gpu_memory_utilization, dtype=dtype, enable_prefix_caching=True) batch_ou
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nses from other requests. bug ### Your current environment ```text vllm version：0.5.0 model: qwen-14b ``` ### 🐛 Describe the bug ``` self.model = LLM(model=model_dir, tokenizer=model_dir, tensor_parallel_size=tensor_par...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: After enabling APC, concurrent processing of requests will result in error and return responses from other requests. bug ### Your current environment ```text vllm version：0.5.0 model: qwen-14b ``` ### 🐛 Describe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
