# vllm-project/vllm#35880: [Bug]: Qwen/Qwen3.5-27B-GPTQ-Int4 not working /tmp/tmpb6zywp4k/__triton_launcher.c:7:10: fatal error: Python.h: No such file or directory     7 | #include <Python.h>

| 字段 | 值 |
| --- | --- |
| Issue | [#35880](https://github.com/vllm-project/vllm/issues/35880) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen/Qwen3.5-27B-GPTQ-Int4 not working /tmp/tmpb6zywp4k/__triton_launcher.c:7:10: fatal error: Python.h: No such file or directory     7 \| #include <Python.h>

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug My code: ``` from vllm import LLM llm_name = "Qwen/Qwen3.5-27B-GPTQ-Int4" llm = LLM( model=llm_name, dtype=torch.bfloat16, trust_remote_code=True, # quantization="bitsandbytes", max_model_len=16384, max_num_seqs=512, seed=0 ) ``` Output: ``` GPU allocated memory: 0.00 GB GPU reserved memory: 0.00 GB Configuring GPU environment... /home/username/absa-toolkit/helper.py:790: FutureWarning: torch.cuda.reset_max_memory_allocated now calls torch.cuda.reset_peak_memory_stats, which resets /all/ peak memory stats. torch.cuda.reset_max_memory_allocated() Configuring GPU environment... INFO 03-03 16:21:05 [utils.py:238] non-default args: {'trust_remote_code': True, 'dtype': torch.bfloat16, 'max_model_len': 16384, 'max_num_seqs': 512, 'disable_log_stats': True, 'model': 'Qwen/Qwen3.5-27B-GPTQ-Int4'} The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. INFO 03-03 16:21:06 [model.py:530]...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Qwen/Qwen3.5-27B-GPTQ-Int4 not working /tmp/tmpb6zywp4k/__triton_launcher.c:7:10: fatal error: Python.h: No such file or directory 7 | #include <Python.h> bug ### Your current environment ### 🐛 Describe the bug
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: r current environment ### 🐛 Describe the bug My code: ``` from vllm import LLM llm_name = "Qwen/Qwen3.5-27B-GPTQ-Int4" llm = LLM( model=llm_name, dtype=torch.bfloat16, trust_remote_code=True, # quantization="bitsandbyte...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: Qwen/Qwen3.5-27B-GPTQ-Int4 not working /tmp/tmpb6zywp4k/__triton_launcher.c:7:10: fatal error: Python.h: No such file or directory 7 | #include <Python.h> bug ### Your current environment ### 🐛 Describe the bug M...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Qwen/Qwen3.5-27B-GPTQ-Int4 not working /tmp/tmpb6zywp4k/__triton_launcher.c:7:10: fatal error: Python.h: No such file or directory 7 | #include <Python.h> bug ### Your current environment ### 🐛 Describe the bug M...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: ched_tokens=16384. INFO 03-03 16:21:06 [config.py:544] Setting attention block size to 784 tokens to ensure that attention page size is >= mamba page size. INFO 03-03 16:21:06 [config.py:575] Padding mamba page size by...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
