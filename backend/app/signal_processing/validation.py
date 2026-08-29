import numpy as np


def calculate_validation_metrics(detected_peaks, ground_truth_peaks, tolerance=50):
    detected = np.array(detected_peaks)
    ground_truth = np.array(ground_truth_peaks)
    
    if len(detected) == 0 and len(ground_truth) == 0:
        return {
            'precision': 1.0,
            'recall': 1.0,
            'true_positive_count': 0,
            'false_positive_count': 0,
            'false_negative_count': 0
        }
    
    if len(detected) == 0:
        return {
            'precision': 0.0,
            'recall': 0.0,
            'true_positive_count': 0,
            'false_positive_count': 0,
            'false_negative_count': len(ground_truth)
        }
    
    if len(ground_truth) == 0:
        return {
            'precision': 0.0,
            'recall': 0.0,
            'true_positive_count': 0,
            'false_positive_count': len(detected),
            'false_negative_count': 0
        }
    
    matched_gt = set()
    true_positives = 0
    
    for det_peak in detected:
        distances = np.abs(ground_truth - det_peak)
        closest_idx = np.argmin(distances)
        closest_distance = distances[closest_idx]
        
        #Matched peaks
        if closest_distance <= tolerance and closest_idx not in matched_gt:
            true_positives += 1
            matched_gt.add(closest_idx)
    
    # False positives
    false_positives = len(detected) - true_positives
    
    # False negatives
    false_negatives = len(ground_truth) - true_positives
    
    # Calculate metrics
    precision = true_positives / len(detected) if len(detected) > 0 else 0.0
    recall = true_positives / len(ground_truth) if len(ground_truth) > 0 else 0.0
    
    return {
        'precision': round(precision, 4),
        'recall': round(recall, 4),
        'true_positive_count': true_positives,
        'false_positive_count': false_positives,
        'false_negative_count': false_negatives
    }
