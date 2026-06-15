# vllm-project/vllm#5113: [Bug]: Crash sometimes using LLM entrypoint and LoRA adapters

| 字段 | 值 |
| --- | --- |
| Issue | [#5113](https://github.com/vllm-project/vllm/issues/5113) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;sampling_logits;scheduler_memory |
| 子分类 | install |
| Operator 关键词 | sampling |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crash sometimes using LLM entrypoint and LoRA adapters

### Issue 正文摘录

### Your current environment ```text File "/pkg/modal/_container_io_manager.py", line 488, in handle_input_exception yield File "/pkg/modal/_container_entrypoint.py", line 260, in run_input value = await res File "/root/modal_exp_auto_wow_predictions_client.py", line 75, in complete_adapter_prompts results = llm.generate(prompts, sampling_params, lora_request=lora_request) File "/opt/conda/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 214, in generate return self._run_engine(use_tqdm) File "/opt/conda/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 242, in _run_engine step_outputs = self.llm_engine.step() File "/opt/conda/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 557, in step seq_group_metadata_list, scheduler_outputs = self.scheduler.schedule() File "/opt/conda/lib/python3.10/site-packages/vllm/core/scheduler.py", line 890, in schedule scheduler_outputs = self._schedule() File "/opt/conda/lib/python3.10/site-packages/vllm/core/scheduler.py", line 863, in _schedule return self._schedule_default() File "/opt/conda/lib/python3.10/site-packages/vllm/core/scheduler.py", line 722, in _schedule_default remaining_running, running_scheduled =...

## 现有链接修复摘要

#5164 [Bugfix] Fix KeyError: 1 When Using LoRA adapters

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: l.Image.from_registry("pytorch/pytorch:2.2.1-cuda12.1-cudnn8-devel").apt_install("git") #.debian_slim() .pip_install( "vllm==0.4.1", "torch==2.2.1", "transformers==4.40.1", "huggingface_hub==0.19.4", "hf-transfer==0.1.4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 0.4.1", "torch==2.2.1", "transformers==4.40.1", "huggingface_hub==0.19.4", "hf-transfer==0.1.4", ).pip_install("setuptools==65.5","packaging==23.2","ninja==1.11.1.1").pip_install("flash-attn==2.5.8", "--no-build-isolati...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: on modal that is used: modal.Image.from_registry("pytorch/pytorch:2.2.1-cuda12.1-cudnn8-devel").apt_install("git") #.debian_slim() .pip_install( "vllm==0.4.1", "torch==2.2.1", "transformers==4.40.1", "huggingface_hub==0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: dapter_prompts results = llm.generate(prompts, sampling_params, lora_request=lora_request) File "/opt/conda/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 214, in generate return self._run_engine(use_tqdm)...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ite-packages/vllm/engine/llm_engine.py", line 557, in step seq_group_metadata_list, scheduler_outputs = self.scheduler.schedule() File "/opt/conda/lib/python3.10/site-packages/vllm/core/scheduler.py", line 890, in sched...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5164](https://github.com/vllm-project/vllm/pull/5164) | closes_keyword | 0.95 | [Bugfix] Fix KeyError: 1 When Using LoRA adapters  | FIX #5113 During batch inference, when using LoRA adapters, the process crashes due to attempting to remove a LoRA adapter that has already been removed. To address this proble |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
