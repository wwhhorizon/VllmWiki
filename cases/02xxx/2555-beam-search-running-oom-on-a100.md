# vllm-project/vllm#2555: Beam search running OOM on A100

| 字段 | 值 |
| --- | --- |
| Issue | [#2555](https://github.com/vllm-project/vllm/issues/2555) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;sampling |
| 症状 | build_error;crash;mismatch;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Beam search running OOM on A100

### Issue 正文摘录

I'm running a beam search with CodeLlama 34B with max length 2048, as follows: ``` python main.py \ --model codellama/CodeLlama-34b-hf \ --use_auth_token \ --trust_remote_code \ --tasks code_verification \ --batch_size 2 \ --n_samples 2 \ --max_length_generation 2048 \ --precision bf16 \ --save_generations \ --top_p 1 \ --top_k -1 \ --temperature 0 \ --best_of 2 \ --dataset_path $dataset_path \ --use_beam_search \ --exc \ --tensor_parallel_size 2 ``` I'm getting OOM when initializing the engine. Any idea what might be the issue? I also tried with tensor_parallel_size 1, but it's OOM for sequence length over ~1200ish. If I switch batch_size to 1, it seems not to give me the top 2 most likely completions (only gives me the top 1 but repeated twice). ``` Traceback (most recent call last): File "/net/vast-storage/scratch/vast/tenenbaum/gua/Documents/verify/inference/main.py", line 253, in main() File "/net/vast-storage/scratch/vast/tenenbaum/gua/Documents/verify/inference/main.py", line 199, in main model = LLM( File "/scratch2/weka/tenenbaum/gua/anaconda3/envs/cruxeval/lib/python3.9/site-packages/vllm/entrypoints/llm.py", line 105, in __init__ self.llm_engine = LLMEngine.from_engine_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: size 2 \ --n_samples 2 \ --max_length_generation 2048 \ --precision bf16 \ --save_generations \ --top_p 1 \ --top_k -1 \ --temperature 0 \ --best_of 2 \ --dataset_path $dataset_path \ --use_beam_search \ --exc \ --tenso...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Beam search running OOM on A100 I'm running a beam search with CodeLlama 34B with max length 2048, as follows: ``` python main.py \ --model codellama/CodeLlama-34b-hf \ --use_auth_token \ --trust_remote_code \
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Beam search running OOM on A100 I'm running a beam search with CodeLlama 34B with max length 2048, as follows: ``` python main.py \ --model codellama/CodeLlama-34b-hf \ --use_auth_token \ --trust_remote_code \ --tasks c...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ch_size 2 \ --n_samples 2 \ --max_length_generation 2048 \ --precision bf16 \ --save_generations \ --top_p 1 \ --top_k -1 \ --temperature 0 \ --best_of 2 \ --dataset_path $dataset_path \ --use_beam_search \ --exc \ --te...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: \ --n_samples 2 \ --max_length_generation 2048 \ --precision bf16 \ --save_generations \ --top_p 1 \ --top_k -1 \ --temperature 0 \ --best_of 2 \ --dataset_path $dataset_path \ --use_beam_search \ --exc \ --tensor_paral...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
