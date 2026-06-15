# vllm-project/vllm#5693: [Bug]: vision chat completion output with odd Instruction/Output prompting.

| 字段 | 值 |
| --- | --- |
| Issue | [#5693](https://github.com/vllm-project/vllm/issues/5693) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vision chat completion output with odd Instruction/Output prompting.

### Issue 正文摘录

### Your current environment ```text git clone https://github.com/vllm-project/vllm.git cd ~/vllm conda create -n vllm -y conda activate vllm conda install python=3.10 -y pip install -e . pip install hf_transfer pip install torchvision ``` latest main afed90a0344b1b0ce6aae46efc630adb489ec769 run: ``` export NCCL_IGNORE_DISABLED_P2P=1 export CUDA_VISIBLE_DEVICES=5 python -m vllm.entrypoints.openai.api_server --port=5063 \ --host=0.0.0.0 --model microsoft/Phi-3-vision-128k-instruct \ --tensor-parallel-size=1 --seed 1234 \ --max-num-batched-tokens=8192 \ --trust-remote-code \ --tensor-parallel-size=1 \ --max-num-batched-tokens=131072 --max-log-len=100 \ --image-input-type=pixel_values \ --image-token-id=32044 \ --image-input-shape="1,3,1008,1344" \ --image-feature-size=1921 \ --download-dir=$HOME/.cache/huggingface/hub &> vllm_phi3_vision.log & ``` ### 🐛 Describe the bug ``` from openai import OpenAI client = OpenAI(base_url='http://localhost:5063/v1') messages1 = [ { 'role': 'user', 'content': [ {'type': 'text', 'text': 'What do you see?'}, {'type': 'image_url', 'image_url': { 'url': 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0a...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ae46efc630adb489ec769 run: ``` export NCCL_IGNORE_DISABLED_P2P=1 export CUDA_VISIBLE_DEVICES=5 python -m vllm.entrypoints.openai.api_server --port=5063 \ --host=0.0.0.0 --model microsoft/Phi-3-vision-128k-instruct \ --t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: activate vllm conda install python=3.10 -y pip install -e . pip install hf_transfer pip install torchvision ``` latest main afed90a0344b1b0ce6aae46efc630adb489ec769 run: ``` export NCCL_IGNORE_DISABLED_P2P=1 export CUDA...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ect/vllm.git cd ~/vllm conda create -n vllm -y conda activate vllm conda install python=3.10 -y pip install -e . pip install hf_transfer pip install torchvision ``` latest main afed90a0344b1b0ce6aae46efc630adb489ec769 r...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: jKKQdqu64BU/extGD161Q8TXWi6v4ssoJ9SkvLH7VKkiQnzjnywynIONmeMdu5r6vApPDR53sfP4unUjiG47tIg+Hv2WfwpcIlxcp9nDGd2GWVy2WwM/dA2nOc8nNbN34isvDUVvPJqLym4mjTE8ZOIw+Hddp/hHP0FJENHsF1bRtGu2SFbffJA1ud8O4ZOTn5/QenTNcF4ou7O/1hizz3MNsjJ...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: KJc7S4zgOwbkHAPtzzVAfCbw4WiA1DUVARvM2GNmc9mHXj8/qMVv3XiLS7WHX1g8Ux3N0tm8doomQqrY3JsCDHy7sFiT0zxUS69Zf8ACQWaNrVm8EWi5nkFwjK1wO5bPLdf8muRSxC+0c1aVSOzObl+DVoYrcxa3cqxJ84y2hIx/CVxx+JOKzJvhFdQhM61aLhyJS8LqEGDg+vPocde+K9Q0a4m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
