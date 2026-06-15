# vllm-project/vllm#23797: [Usage]: InputProcessingError: Failed to prepare inputs for sequence group with request id: 0,

| 字段 | 值 |
| --- | --- |
| Issue | [#23797](https://github.com/vllm-project/vllm/issues/23797) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;quantization;sampling |
| 症状 | crash;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: InputProcessingError: Failed to prepare inputs for sequence group with request id: 0,

### Issue 正文摘录

### Your current environment Qwen/Qwen2.5-VL-7B-Instruct inference fails on nvidia tesla T4 on google colab with the following error. [Colab link for the same](https://colab.research.google.com/drive/1JLUIVm0xG3eKJT5NINDxngEQ1WB2UOdt?usp=sharing). ``` Adding requests: 100% 1/1 [00:09 1181 self.builder.add_seq_group(seq_group_metadata) 1182 except Exception as e: 17 frames [/usr/local/lib/python3.12/dist-packages/vllm/worker/model_runner.py](https://localhost:8080/#) in add_seq_group(self, seq_group_metadata) 740 for per_seq_group_fn in self.per_seq_group_compute_fns: --> 741 per_seq_group_fn(inter_data, seq_group_metadata) 742 [/usr/local/lib/python3.12/dist-packages/vllm/worker/model_runner.py](https://localhost:8080/#) in _compute_multi_modal_input(self, inter_data, seq_group_metadata) 693 mrope_input_positions, mrope_position_delta = \ --> 694 MRotaryEmbedding.get_input_positions( 695 token_ids, [/usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/rotary_embedding/mrope.py](https://localhost:8080/#) in get_input_positions(cls, input_tokens, hf_config, image_grid_thw, video_grid_thw, second_per_grid_ts, context_len, seq_len, audio_feature_lengths, use_audio_in_vid...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: ence group with request id: 0, usage;stale ### Your current environment Qwen/Qwen2.5-VL-7B-Instruct inference fails on nvidia tesla T4 on google colab with the following error. [Colab link for the same](https://colab.re...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ils on nvidia tesla T4 on google colab with the following error. [Colab link for the same](https://colab.research.google.com/drive/1JLUIVm0xG3eKJT5NINDxngEQ1WB2UOdt?usp=sharing). ``` Adding requests: 100% 1/1 [00:09 118...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: args: {'model': 'Qwen/Qwen2-VL-7B-Instruct', 'trust_remote_code': True, 'dtype': torch.float16, 'max_model_len': 16384, 'disable_log_stats': True, 'quantization': 'bitsandbytes'} The argument `trust_remote_code` is to b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: b with the following error. [Colab link for the same](https://colab.research.google.com/drive/1JLUIVm0xG3eKJT5NINDxngEQ1WB2UOdt?usp=sharing). ``` Adding requests: 100% 1/1 [00:09 1181 self.builder.add_seq_group(seq_grou...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: % 1/1 [00:09 1181 self.builder.add_seq_group(seq_group_metadata) 1182 except Exception as e: 17 frames [/usr/local/lib/python3.12/dist-packages/vllm/worker/model_runner.py](https://localhost:8080/#) in add_seq_group(sel...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23801: Should have ROCm label: NO (0 matches) #23797: Should have ROCm label: NO (0 matches) #23796: Should have ROCm label: NO (0 matches) #23794: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
