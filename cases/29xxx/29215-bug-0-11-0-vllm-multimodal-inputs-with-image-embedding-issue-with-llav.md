# vllm-project/vllm#29215: [Bug]: 0.11.0 vllm multimodal inputs with image embedding issue with LlavaNext

| 字段 | 值 |
| --- | --- |
| Issue | [#29215](https://github.com/vllm-project/vllm/issues/29215) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.11.0 vllm multimodal inputs with image embedding issue with LlavaNext

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` def execute_batch_pope_with_pruned_embeddings( modelname: str, fields: List[Dict[str, Any]], query: str, keep_ratio: float, typed_fields: List[Tuple[str, str]], reordered_columns: List[str], system_prompt: str = DEFAULT_SYSTEM_PROMPT, guided_choice: List[str] = None, base_url: str = None, # Not used in offline mode, but kept for signature compatibility ) -> Tuple[List[str], float]: # --- PHASE 1: Pruning / Embedding Generation (PyTorch) --- print("Phase 1: Loading Vision Model for Pruning...") vision_tower, model, processor = load_vision_models_llava_next(device='cuda') user_prompts = [] all_pruned_embeddings = [] batch_pruning_time = 0.0 try: for field_dict in fields: user_prompt = "" pruned_embeddings_for_this_prompt = [] for field_name in reordered_columns: # ... (Existing logic to find field type) ... field_type = next((ft for fn, ft in typed_fields if fn == field_name), None) if field_type == "text": value = field_dict.get(field_name, "") user_prompt += f"{field_name}: {value}\n" elif field_type == "image": # IMPORTANT: vLLM needs the token to know where to inject embeddings user_prompt += f"{field_name}: \n" image_data...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: 0.11.0 vllm multimodal inputs with image embedding issue with LlavaNext bug ### Your current environment ### 🐛 Describe the bug ``` def execute_batch_pope_with_pruned_embeddings( modelname: str, fields: List[Dict...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: elif field_type == "image": # IMPORTANT: vLLM needs the token to know where to inject embeddings user_prompt += f"{field_name}: \n" image_data = field_dict.get(field_name)
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: vision_tower, model, processor = load_vision_models_llava_next(device='cuda') user_prompts = [] all_pruned_embeddings = [] batch_pruning_time = 0.0 try: for field_dict in fields: user_prompt = "" pruned_embeddings_for_t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: lm/entrypoints/llm.py", line 439, in generate self._validate_and_add_requests( File "/scratch/hpc-prf-haqc/haikai/vllm/vllm/entrypoints/llm.py", line 1612, in _validate_and_add_requests raise e File "/scratch/hpc-prf-ha...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: , 3.7384e-03, ..., -2.1839e-04, -1.0376e-03, 3.2959e-03]]], dtype=torch.float16)]} with kwargs={'truncation': False} ``` But when if I put reduce_tokens = reduce_tokens.unsqueeze(0) to transfo rm it back to a 3D tensor,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
