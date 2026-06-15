# vllm-project/vllm#2620: vllm 0.2.7 with tensor-parallel > 1 inference mode in place error 

| 字段 | 值 |
| --- | --- |
| Issue | [#2620](https://github.com/vllm-project/vllm/issues/2620) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> vllm 0.2.7 with tensor-parallel > 1 inference mode in place error 

### Issue 正文摘录

In trying to debug tensor parallel on 0.2.7 and have exhausted possible ideas. Trying to run mixtral 8X7b model which requires 2 gpu devices I have 8X 80GB VRAM A100 cuda machine. ```bash lroberts@GPU77B9:~/llm_quantization$ FLASK_APP=quantized_flask_app.py FLASK_ENV=debug python3.10 -m flask run * Serving Flask app 'quantized_flask_app.py' (lazy loading) * Environment: debug * Debug mode: off /usr/lib/python3/dist-packages/requests/__init__.py:87: RequestsDependencyWarning: urllib3 (2.1.0) or chardet (5.2.0) doesn't match a supported version! warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported " 16384 INFO 2024-01-26 22:13:10,261 abc_etal.py:195 unknown_model_name:unknown_model_version Hello! logging initialized, starting up... INFO 2024-01-26 22:13:10,261 abc_etal.py:196 unknown_model_name:unknown_model_version Git commit of model: unknown_git_commit INFO 2024-01-26 22:13:10,261 abc_etal.py:197 unknown_model_name:unknown_model_version Git commit of cuda torch base: unknown_git_commit INFO 2024-01-26 22:13:11,883 abc_etal.py:200 unknown_model_name:unknown_model_version Compute device available: cuda WARNING 01-26 22:13:14 config.py:506] Casting torch.bfloat16 to...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ode: off /usr/lib/python3/dist-packages/requests/__init__.py:87: RequestsDependencyWarning: urllib3 (2.1.0) or chardet (5.2.0) doesn't match a supported version! warnings.warn("urllib3 ({}) or chardet ({}) doesn't match...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: on 0.2.7 and have exhausted possible ideas. Trying to run mixtral 8X7b model which requires 2 gpu devices I have 8X 80GB VRAM A100 cuda machine. ```bash lroberts@GPU77B9:~/llm_quantization$ FLASK_APP=quantized_flask_app...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: I have 8X 80GB VRAM A100 cuda machine. ```bash lroberts@GPU77B9:~/llm_quantization$ FLASK_APP=quantized_flask_app.py FLASK_ENV=debug python3.10 -m flask run * Serving Flask app 'quantized_flask_app.py' (lazy loading) *...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: run mixtral 8X7b model which requires 2 gpu devices I have 8X 80GB VRAM A100 cuda machine. ```bash lroberts@GPU77B9:~/llm_quantization$ FLASK_APP=quantized_flask_app.py FLASK_ENV=debug python3.10 -m flask run * Serving...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=16384, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=awq, enforce_eager=False, s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
