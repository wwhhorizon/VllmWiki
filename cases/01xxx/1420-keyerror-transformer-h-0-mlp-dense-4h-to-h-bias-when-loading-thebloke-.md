# vllm-project/vllm#1420: KeyError: 'transformer.h.0.mlp.dense_4h_to_h.bias' when loading TheBloke/WizardLM-Uncensored-Falcon-40B-GPTQ on A100-80GB

| 字段 | 值 |
| --- | --- |
| Issue | [#1420](https://github.com/vllm-project/vllm/issues/1420) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> KeyError: 'transformer.h.0.mlp.dense_4h_to_h.bias' when loading TheBloke/WizardLM-Uncensored-Falcon-40B-GPTQ on A100-80GB

### Issue 正文摘录

Error when loading TheBloke/WizardLM-Uncensored-Falcon-40B-GPTQ on a A100-80GB ``` KeyError Traceback (most recent call last) [/home/evilscript/Sync/Projects/LLM-semagram/big_mf_test.ipynb](https://file+.vscode-resource.vscode-cdn.net/home/evilscript/Sync/Projects/LLM-semagram/big_mf_test.ipynb) Cell 5 line 6 [3](vscode-notebook-cell:/home/evilscript/Sync/Projects/LLM-semagram/big_mf_test.ipynb#W4sZmlsZQ%3D%3D?line=2) file_output = f'{f_m_name}__t_{t}__top_p_{top_p}__max_new_tokens_{max_new_tokens}.jsonl' [5](vscode-notebook-cell:/home/evilscript/Sync/Projects/LLM-semagram/big_mf_test.ipynb#W4sZmlsZQ%3D%3D?line=4) print(f'Running {model_name} with {num_prompts} prompts') ----> [6](vscode-notebook-cell:/home/evilscript/Sync/Projects/LLM-semagram/big_mf_test.ipynb#W4sZmlsZQ%3D%3D?line=5) model = LLM(model_name, trust_remote_code=True) # gpu_memory_utilization=0.93 [8](vscode-notebook-cell:/home/evilscript/Sync/Projects/LLM-semagram/big_mf_test.ipynb#W4sZmlsZQ%3D%3D?line=7) with open(file_output, 'w') as writer: [9](vscode-notebook-cell:/home/evilscript/Sync/Projects/LLM-semagram/big_mf_test.ipynb#W4sZmlsZQ%3D%3D?line=8) generator = prompt_generator(input_f) File [/usr/local/lib/pyth...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: /LLM-semagram/big_mf_test.ipynb#W4sZmlsZQ%3D%3D?line=4) print(f'Running {model_name} with {num_prompts} prompts') ----> [6](vscode-notebook-cell:/home/evilscript/Sync/Projects/LLM-semagram/big_mf_test.ipynb#W4sZmlsZQ%3D...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: st recent call last) [/home/evilscript/Sync/Projects/LLM-semagram/big_mf_test.ipynb](https://file+.vscode-resource.vscode-cdn.net/home/evilscript/Sync/Projects/LLM-semagram/big_mf_test.ipynb) Cell 5 line 6 [3](vscode-no...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: del, tokenizer, tokenizer_mode, trust_remote_code, tensor_parallel_size, dtype, quantization, revision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, **kwargs) 77 kwargs["disable_log_stats"] = True 78 en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: _to_h.bias' when loading TheBloke/WizardLM-Uncensored-Falcon-40B-GPTQ on A100-80GB Error when loading TheBloke/WizardLM-Uncensored-Falcon-40B-GPTQ on a A100-80GB ``` KeyError Traceback (most recent call last) [/home/evi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 3 self.llm_engine = LLMEngine.from_engine_args(engine_args) 94 self.request_counter = Counter() File [/usr/local/lib/python3.9/dist-packages/vllm/engine/llm_engine.py:231](https://file+.vscode-resource.vscode-cdn.net/us...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
