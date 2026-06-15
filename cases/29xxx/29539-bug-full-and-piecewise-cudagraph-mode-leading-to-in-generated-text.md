# vllm-project/vllm#29539: [Bug]: FULL_AND_PIECEWISE cudagraph mode leading to !!! in generated text

| 字段 | 值 |
| --- | --- |
| Issue | [#29539](https://github.com/vllm-project/vllm/issues/29539) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FULL_AND_PIECEWISE cudagraph mode leading to !!! in generated text

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We observed !!! in generated text, indicating there are NaNs in logits. After some debugging, we found it's related to FULL_AND_PIECEWISE cudagraph mode. I was running on p5e machine (H200), using vllm/vllm-openai:v0.11.2 container. Command to reproduce: ``` VLLM_ATTENTION_BACKEND=TRITON_ATTN vllm serve openai/gpt-oss-20b \ --tensor-parallel-size 8 \ --max-num-seqs 16 ``` ``` python3 -m lm_eval --model local-completions \ --model_args model=openai/gpt-oss-20b,base_url=http://127.0.0.1:8000/v1/completions,num_concurrent=16 \ --tasks gsm8k \ --log_samples --output_path /tmp/lm_eval/ ``` There are a lot of !!! in output resps. ``` $ grep "\!\!\!" /tmp/lm_eval/openai__gpt-oss-20b/samples_gsm8k_2025-11-26T11-32-23.652532.jsonl {"doc_id": 43, "doc": {"question": "According to its nutritional info, a bag of chips has 250 calories per serving. If a 300g bag has 5 servings, how many grams can you eat if your daily calorie target is 2000 and you have already consumed 1800 calories?", "answer": "If the total calorie target is 2000 and I have consumed 1800 calories then I have 2000-1800 = >200 calories left to eat\nIf each serving of chips h...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: FULL_AND_PIECEWISE cudagraph mode leading to !!! in generated text bug ### Your current environment ### 🐛 Describe the bug We observed !!! in generated text, indicating there are NaNs in logits. After some debugg...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: two times more blue balls. Later on, he lost 6 of the red balls, so he decided to buy some yellow balls to fill up his collection. How many yellow balls did he buy if, after all, he had 74 balls in total?\nAnswer: Jamie...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: to reproduce: ``` VLLM_ATTENTION_BACKEND=TRITON_ATTN vllm serve openai/gpt-oss-20b \ --tensor-parallel-size 8 \ --max-num-seqs 16 ``` ``` python3 -m lm_eval --model local-completions \ --model_args model=openai/gpt-oss-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: vllm-openai:v0.11.2 container. Command to reproduce: ``` VLLM_ATTENTION_BACKEND=TRITON_ATTN vllm serve openai/gpt-oss-20b \ --tensor-parallel-size 8 \ --max-num-seqs 16 ``` ``` python3 -m lm_eval --model local-completio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: --tensor-parallel-size 8 \ --max-num-seqs 16 ``` ``` python3 -m lm_eval --model local-completions \ --model_args model=openai/gpt-oss-20b,base_url=http://127.0.0.1:8000/v1/completions,num_concurrent=16 \ --tasks gsm8k \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
